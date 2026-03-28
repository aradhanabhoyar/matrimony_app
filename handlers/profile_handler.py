import tornado.web
import tornado.escape  

from utils.db import SessionLocal
from models.profile_model import Profile   

from utils.response import success, error
from utils.middleware import get_current_user


class ProfileHandler(tornado.web.RequestHandler):

    # 🔹 CREATE PROFILE
    def post(self):
        user_data = get_current_user(self)

        if not user_data:
            self.set_status(401)
            self.write(error("Unauthorized"))
            return

        data = tornado.escape.json_decode(self.request.body)
        db = SessionLocal()

        try:
            # Optional: prevent duplicate profile
            existing = db.query(Profile).filter_by(user_id=user_data["user_id"]).first()
            if existing:
                self.set_status(400)
                self.write(error("Profile already exists"))
                return

            profile = Profile(
                user_id=user_data["user_id"],
                age=data.get("age"),
                gender=data.get("gender"),
                religion=data.get("religion"),
                city=data.get("city")
            )

            db.add(profile)
            db.commit()

            self.write(success("Profile created"))

        except Exception as e:
            self.set_status(500)
            self.write(error(str(e)))

        finally:
            db.close()


    # 🔹 UPDATE PROFILE
    def put(self):
        user_data = get_current_user(self)

        if not user_data:
            self.set_status(401)
            self.write(error("Unauthorized"))
            return

        data = tornado.escape.json_decode(self.request.body)
        db = SessionLocal()

        try:
            profile = db.query(Profile).filter_by(user_id=user_data["user_id"]).first()

            if not profile:
                self.set_status(404)
                self.write(error("Profile not found"))
                return

            # update fields only if provided
            profile.age = data.get("age", profile.age)
            profile.gender = data.get("gender", profile.gender)
            profile.religion = data.get("religion", profile.religion)
            profile.city = data.get("city", profile.city)

            db.commit()

            self.write(success("Profile updated"))

        except Exception as e:
            self.set_status(500)
            self.write(error(str(e)))

        finally:
            db.close()


    # 🔹 DELETE PROFILE
    def delete(self):
        user_data = get_current_user(self)

        if not user_data:
            self.set_status(401)
            self.write(error("Unauthorized"))
            return

        db = SessionLocal()

        try:
            profile = db.query(Profile).filter_by(user_id=user_data["user_id"]).first()

            if not profile:
                self.set_status(404)
                self.write(error("Profile not found"))
                return

            db.delete(profile)
            db.commit()

            self.write(success("Profile deleted"))

        except Exception as e:
            self.set_status(500)
            self.write(error(str(e)))

        finally:
            db.close()


class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        db = SessionLocal()

        try:
            query = db.query(Profile)

            age_min = self.get_argument("age_min", None)
            age_max = self.get_argument("age_max", None)
            city = self.get_argument("city", None)

            if age_min:
                query = query.filter(Profile.age >= int(age_min))

            if age_max:
                query = query.filter(Profile.age <= int(age_max))

            if city:
                query = query.filter(Profile.city == city)

            results = query.all()

            data = [
                {
                    "age": p.age,
                    "city": p.city,
                    "religion": p.religion
                }
                for p in results
            ]

            self.write(success("Profiles fetched", data))

        except Exception as e:
            self.set_status(500)
            self.write(error(str(e)))

        finally:
            db.close()
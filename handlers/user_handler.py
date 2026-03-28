import tornado.web
import tornado.escape  

from utils.db import SessionLocal
from models.user_model import User
from utils.auth import generate_token

import bcrypt
from utils.response import success, error

class RegisterHandler(tornado.web.RequestHandler):
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        db = SessionLocal()

        try:
            name = data.get("name")
            email = data.get("email")
            password = data.get("password")

            if not all([name, email, password]):
                self.set_status(400)
                self.write(error("All fields required"))
                return

            if db.query(User).filter_by(email=email).first():
                self.set_status(400)
                self.write(error("Email already exists"))
                return

            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

            user = User(name=name, email=email, password=hashed.decode())
            db.add(user)
            db.commit()

            self.write(success("User registered"))

        except Exception as e:
            self.set_status(500)
            self.write(error(str(e)))

        finally:
            db.close()

class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        db = SessionLocal()

        try:
            email = data.get("email")
            password = data.get("password")

            user = db.query(User).filter_by(email=email).first()

            if not user or not bcrypt.checkpw(password.encode(), user.password.encode()):
                self.set_status(401)
                self.write(error("Invalid credentials"))
                return

            token = generate_token(user.id)

            self.write(success("Login successful", {"token": token}))

        except Exception as e:
            self.set_status(500)
            self.write(error(str(e)))

        finally:
            db.close()



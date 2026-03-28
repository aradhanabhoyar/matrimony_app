import tornado.web 
from handlers.user_handler import RegisterHandler, LoginHandler
from handlers.profile_handler import ProfileHandler, SearchHandler

def make_app():
    return tornado.web.Application([
        (r"/register", RegisterHandler),
        (r"/login", LoginHandler),
        (r"/profile", ProfileHandler),
        (r"/search", SearchHandler),
    ])
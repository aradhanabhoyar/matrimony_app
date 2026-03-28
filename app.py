import tornado.ioloop
from routes import make_app
from utils.db import create_tables

create_tables()   
app = make_app()
app.listen(8888)
print("Server running on http://localhost:8888")
tornado.ioloop.IOLoop.current().start()
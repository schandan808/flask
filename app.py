from flask import Flask
from flask_pymongo import PyMongo
from router.router import main_route

app =Flask(__name__)

app.register_blueprint(main_route, url_prefix='/')
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
if __name__ == '__main__':
    app.debug = True
    app.run()
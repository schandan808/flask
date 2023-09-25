from flask import Flask
from pymongo import MongoClient
from router.router import main_route
from flask_cors import CORS

app =Flask(__name__)
CORS(app)
app.register_blueprint(main_route, url_prefix='/')

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = MongoClient(app.config['MONGO_URI'])


if __name__ == '__main__':
    app.debug = True
    app.run()
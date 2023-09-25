from flask import Flask
from router.router import main_route
from flask_cors import CORS

app =Flask(__name__)
CORS(app)
app.register_blueprint(main_route, url_prefix='/')

if __name__ == '__main__':
    app.debug = True
    app.run()
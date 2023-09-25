from flask import Blueprint ,jsonify
from helper import helper 
from controller import userController

main_route = Blueprint("main_router",__name__)

@main_route.route('/')
def index():
    try: 
        data = userController.getData()
        return helper.success(data,"success data")
    except Exception as e:
        error_message = str(e)
        return helper.failed(error_message,"faild")

@main_route.route('/test')
def userData(data):
    try :
        print()
    except:
        print("An exception occurred")


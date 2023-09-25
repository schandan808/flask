from flask import Blueprint ,jsonify,request
from helper import helper 
from controller import userController

main_route = Blueprint("main_router",__name__)

@main_route.route('/',methods=['GET'])
def index():
    try: 
        data = userController.getData()
        return helper.success(data,"success data")
    except Exception as e:
        error_message = str(e)
        return helper.failed(error_message,"faild")

@main_route.route('/test',methods=['POST'])
def userData():
    try :
        data = request.json
        userc = userController.createUser(data)    
        return helper.success(userc,"success")
    except Exception as e:
        error_message = str(e)
        return helper.failed(error_message,"faild")


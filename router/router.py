from flask import Blueprint 
from helper import helper 
from controller import userController

main_route = Blueprint("main_router",__name__)


@main_route.route('/')
def index():
    try: 
        print()

    except:
        print()    
    # data = userController.getData()
    # return helper.success(data,"success data")


@main_route.route('/test',)
def userData(data):
    try :
        print()
    except:
        print("An exception occurred")


from pymongo import MongoClient
from helper import helper
mongo_uri = "mongodb://127.0.0.1:27017/"
client = MongoClient(mongo_uri)
db = client["myDatabase"]
usersModel = db['users']

def getData():
    try:
        data = usersModel.find_one({"email": "test@gmail.com"})
        if data ==None :
            newData = usersModel.insert_one({
                'name': 'John Doe',
                'age': 30,
                'city': 'New York',
                "email": "test@gmail.com"
            })
            newData =str(newData.inserted_id)
            print(newData)
            return newData
        else:
            data["_id"]=str(data["_id"])
            return data    
      
    except Exception as e:
        error_message = str(e)
        print(error_message, '====error')
        return helper.failed(error_message, "error")

def createUser(data) :
    try:
        print(data)
        return data   
    except Exception as e :
        error_msg =str(e)
        return helper.failed(error_msg ,"faild")   

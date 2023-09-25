from models.user import User

def getData():
    try:
        # data = User.find_one({"email":"test@gmail.com"})
        # print(data,'=====')
        return  {
            'name': 'John Doe',
            'age': 30,
            'city': 'New York'
        }
    except Exception as e :
        error_message = str(e)
        return print(error_message,'====error')    
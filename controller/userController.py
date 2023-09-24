from models import User

def getData():

    data = User.find_one({"email":"test@gmail.com"})
    print(data,'=====')
    return  {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
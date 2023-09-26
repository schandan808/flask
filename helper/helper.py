from flask import jsonify
import random

def success(data,msg) :
   return jsonify({"status":200 ,"msg":msg,"data":data})

def failed(data,msg) :
   return jsonify({"status":400 ,"msg":msg,"error":data})

def randomNuber():
  random_number = random.randint(1000, 9999)
  print(random_number)
  return random_number

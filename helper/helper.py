from flask import jsonify

def success(data,msg) :
   return jsonify({"status":200 ,"msg":msg,"data":data})

def failed(data,msg) :
   return jsonify({"status":400 ,"msg":msg,"error":data})

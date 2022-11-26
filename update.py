from flask import Flask, request, jsonify
import pymongo
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps
# from werkzeug.security im/port generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/check"
mongo = PyMongo(app)
table = mongo.db.user


@app.route('/add', methods=["POST"])
def create():
    _form = request.form

    _name = _form["name"]
    _number = _form["number"]

    if _name and _number and request.method == 'POST':
        table.insert_one({'name': _name, 'number': _number})
        resp = jsonify("User create successfully")
        resp.status_code = 200
        return resp


@app.route('/update/<string:name>', methods=["PUT"])
def UpdateUser(name):
    _form = request.form
    _name = _form['name']
    _number = _form["number"]
    if _name and _number and request.method == "PUT":
        table.update_one({'name': name}, {"$set": {'name': _name, "number": _number}})
        resp = jsonify("User update  successfully")
        resp.status_code = 200
        return resp


@app.route('/find/<string:name>', methods=["GET"])
def findUser(name):
    user = table.find_one({"name": name})
    resp = dumps(user)

    return resp


@app.route("/delete/<string:name>", methods=["DELETE"])
def deleteuser(name):
    table.delete_one({"name": name})
    resp = jsonify("User deleted successfully")
    resp.status_code = 200
    return resp


# for checking
# @app.route('/check', methods=['GET', 'POST'])
# def check():
#     _form = request.form
#
#     _name = _form["name"]
#     _number = _form["number"]
#     if _name and request.method == 'GET':
#         a = table.find_one({"name": _name})
#         resp = dumps(a)
#         if resp == "null":
#             if _name and _number and request.method == "POST":
#                 mongo.db.user.insert_one({"name": _name, "number": _number})
#                 resp = jsonify("User create successfully")
#                 resp.status_code = 200
#                 return resp
#
#         elif resp != "null":
#             return "user already exits"

@app.route('/check', methods=['POST'])
def check():
    _form = request.form
    _name = _form["name"]
    _number = _form["number"]
    a = mongo.db.user.find_one({"name": _name}, {"name": 1, "_id": 0, })
    resp = dumps(a)
    print(resp)
    if _name in resp:
        return "User already exist"
    elif _name and _number and request.method == "POST":
        mongo.db.user.insert_one({"name": _name, "number": _number})
        resp = jsonify("user create successfully")
        resp.status_code = 200
        return resp


if __name__ == '__main__':
    app.run(debug=True)

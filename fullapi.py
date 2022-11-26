import _json


import pymongo
from flask_pymongo import PyMongo

from flask import Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail

app = Flask(__name__)
app.secret_key = "secretkey"
app.config['MONGO_URI'] = "mongodb://localhost:27017/blog"
mongo = PyMongo(app)


@app.route('/super', methods=['POST'])
def add_user():
    # send data by form-data
    _form = request.form
    _name = _form['name']
    _email = _form['email']
    _password = _form['password']

    # send data by the json
    # _json = request.json
    # _name = _json["name"]
    # _email = _json["email"]
    # _password = _json["password"]
    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)
        mongo.db.simpleblog.insert_one({'name': _name, 'email': _email, 'password': _hashed_password, })
        resp = jsonify("User add Successfully")
        resp.status_code = 200
        return resp
    # else:
    #     not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Fount' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@app.route('/users', )
def users():
    user = mongo.db.simpleblog.find()
    resp = dumps(user)
    return resp


@app.route('/user/<id>')
def user(id):
    user = mongo.db.simpleblog.find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp


@app.route('/getdata/<email>')
def userdata(email):
    user1 = mongo.db.simpleblog.find_one({'email': email})
    resp = dumps(user1)
    return resp


@app.route('/delete/<email>', methods=['DELETE'])
def delUser(email):
    mongo.db.simpleblog.delete_one({'email': email})
    resp = jsonify("User successfully delete")
    resp.status_code = 200
    return resp


@app.route('/update/<email>', methods=['PUT'])
def updateUser(email):

    _form = request.json
    _id = id
    _name = _form['name']
    _email = _form['email']
    _password = _form['password']
    if _name and _email and _password and request.method == 'PUT':
        _hashed_password = generate_password_hash(_password)
        # mongo.db.simpleblog.update_one({'_id': ObjectId(_id['oid']) if '$oid' in _id else ObjectId()},
        #                            {'$set': {'name': _name, 'email': _email, 'password': _hashed_password}})
        mongo.db.simpleblog.update_one()

        resp = jsonify("User update successfully")
        resp.set_data = 200
        return resp
    else: return  not_found()

#
# @app.route('/update/<id>', methods=['PUT'])
# def update_user(id):
#     _json = request.form
#     _id = _json['_id']
#     _name = _json['name']
#     _email = _json['email']
#     _password = _json['password']
#     # validate the received values
#     if _name and _email and _password and _id and request.method == 'PUT':
#         # do not save password as a plain text
#         _hashed_password = generate_password_hash(_password)
#         # save edits
#         mongo.db.simpleblog.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},
#                                  {'$set': {'name': _name, 'email': _email, 'password': _hashed_password}})
#         resp = jsonify('User updated successfully!')
#         resp.status_code = 200
#         return resp
#     else:
#         return not_found()


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request, session
from flask_pymongo import PyMongo
from bson.json_util import dumps
from werkzeug.security import generate_password_hash, check_password_hash
from time import sleep

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/check"
mongo = PyMongo(app)
database = mongo.db.flutter
app.secret_key = "super secret key"


# _from = request.form
# _name = _from["name"]
# _email = _from["email"]
# _number = _from["number"]
# _password = _from["password"]
# hashcode = generate_password_hash(_password)


@app.route("/add", methods=["POST", ])
def create():
    _from = request.form
    _name = _from["name"]
    _email = _from["email"]
    _number = _from["number"]
    _password = _from["password"]

    hashcode = generate_password_hash(_password)
    data = database.find_one({"email": _email}, )
    resp = dumps(data)
    print(resp)
    if _email in resp:
        # print(_password)
        # print(hashcode)
        # print(decode)
        return "User already exist"
    elif _name and _email and _number and _password and request.method == "POST":
        database.insert_one({"name": _name, "email": _email, "number": _number, "password": hashcode})
        resp = jsonify("User create successfully")
        resp.status_code = 200
        # print(_password)
        # print(hashcode)
        # print(decode)
        return resp


@app.route('/userList', methods=['GET'])
def userGet():
    users = database.find()
    resp = dumps(users)
    return resp


@app.route("/oneUser/<string:name>", methods=["GET"])
def oneUser(name):
    # _from = request.form
    # _name = _from["name"]

    one_user = database.find_one({"name": name})
    resp = dumps(one_user)
    if name in resp:
        return resp
    else:
        return "User not exist"


@app.route("/one", methods=["GET"])
def one():
    # _from = request.form
    _name = request.form["name"]
    one_user = database.find_one({"name": _name})
    resp = dumps(one_user)
    if _name in resp:
        return resp
    else:
        return "User not exist"


@app.route("/password", methods=["GET"])
def password():
    _name = request.form["name"]
    _password = request.form["password"]

    data = database.find_one({"name": _name, }, {"password": 1, "_id": 0})
    resp = dumps(data)


@app.route("/check", methods=["GET", "POST"])
def check():
    if request.method == "POST":
        # _name = request.form["name"]
        _email = request.form["email"]
        # _number = request.form["number"]
        _password = request.form["password"]
        # generate_password_hash(_password)
        data = database.courses.find_one({ "email": _email,  "password": _password})
        # pas = data.password
        # if _password == pas:
        #     print(pas)
        session["email"]= _email
        resp = dumps(data)
        # resp.status_code = 200
        return  resp
        # return  pas

if __name__ == '__main__':
    app.run(debug=True)

import pymongo

from flask import  Flask, request, jsonify
from  bson.json_util import  dumps
from bson.objectid import ObjectId
from  werkzeug.security import  generate_password_hash,check_password_hash


app = Flask(__name__)
app.secret_key = "secretkey"

if __name__ == '__main__':
    print("Welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/lucky")
    print(client)
    alldb = client.list_database_names()
    print(alldb)
    db = client['lucky']
    collections = db['thisIsLucky']
    # dictionary = {
    #     'name': "lucky",
    #     'mask': 45,
    # }
    #
    # collections.insert_one(dictionary)
    # dictionary2 = {
    #     'name': "ayush",
    #     'mask': 445,
    # }
    #
    # collections.insert_one(dictionary2)
    #insert many//////////
    # insertThese = [
    #     {'_id': 1, 'name': "khushi", 'location': 'kanpur', 'mask': 77},
    #     {'_id': 3,'name': "deepika", 'location': 'deli', 'mask': 65},
    #     {'_id': 2,'name': "hitesk", 'location': 'jaipur', 'mask': 45}
    # ]
    # collections.insert_many(insertThese)
    #find one
    # one = collections.find_one({'name':'lucky'})
    allDoc = collections.find({'name': 'lucky'},{'name': 1,'_id':0})
    for item in allDoc:
        print(item)
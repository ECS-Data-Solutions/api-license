from flask_restful import Resource
from flask import request
from random import randbytes
from elicense.mongo import mongo

class CancelLicense(Resource):
    def delete(self):
        license_key = request.json['license_key']
        license = mongo.db.licenses.find_one({"license_key": license_key})
        if license:
            mongo.db.licenses.delete_one({"license_key": license_key})
            return license, 200
        return "License not found", 404
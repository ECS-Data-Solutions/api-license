from flask_restful import Resource
from flask import request
from random import randbytes
from elicense.__init__ import mongo

class CheckLicense(Resource):
    def get(self):
        license_key = request.json['license_key']
        license = mongo.db.licenses.find_one({"license_key": license_key})
        if license:
            if license['in_use']:
                return license, 200
            else:
                return "License not in use", 404
        return "License not found", 404
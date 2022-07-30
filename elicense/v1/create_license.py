from flask_restful import Resource
from flask import request
from random import randbytes
from elicense.__init__ import mongo


class CreateLicense(Resource):
    def post(self):

        user_id = request.json['user_id']
        activated = True
        license_key = randbytes(32).hex()
        in_use = False

        license = {"user_id": user_id, "activated": activated, "license_key": license_key, "in_use": in_use}

        mongo.db.licenses.insert_one(license)
        return license, 200

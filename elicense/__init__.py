from flask import Flask
from flask_restful import Api
import os
from flask_pymongo import PyMongo


app = Flask(__name__)
api = Api(app)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

# API /v1
from .v1.activate_license import ActivateLicense
from .v1.cancel_license import CancelLicense
from .v1.check_license import CheckLicense
from .v1.create_license import CreateLicense
from .v1.deactivate_license import DeactivateLicense
from .v1.expire_license import ExpireLicense
from .v1.renew_license import RenewLicense

api.add_resource(ActivateLicense, '/v1/activate_license')
api.add_resource(CancelLicense, '/v1/cancel_license')
api.add_resource(CheckLicense, '/v1/check_license')
api.add_resource(CreateLicense, '/v1/create_license')
api.add_resource(DeactivateLicense, '/v1/deactivate_license')
api.add_resource(ExpireLicense, '/v1/expire_license')
api.add_resource(RenewLicense, '/v1/renew_license')


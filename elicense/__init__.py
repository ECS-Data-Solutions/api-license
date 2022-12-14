from flask import Flask
from flask_restful import Api
import os


app = Flask(__name__)
api = Api(app)

# API /v1
from elicense.v1.activate_license import ActivateLicense
from elicense.v1.cancel_license import CancelLicense
from elicense.v1.check_license import CheckLicense
from elicense.v1.create_license import CreateLicense
from elicense.v1.deactivate_license import DeactivateLicense
from elicense.v1.expire_license import ExpireLicense
from elicense.v1.renew_license import RenewLicense

api.add_resource(ActivateLicense, '/v1/activate_license')
api.add_resource(CancelLicense, '/v1/cancel_license')
api.add_resource(CheckLicense, '/v1/check_license')
api.add_resource(CreateLicense, '/v1/create_license')
api.add_resource(DeactivateLicense, '/v1/deactivate_license')
api.add_resource(ExpireLicense, '/v1/expire_license')
api.add_resource(RenewLicense, '/v1/renew_license')


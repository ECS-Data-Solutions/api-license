from pymongo import MongoClient
import os

mongo = MongoClient(os.getenv('MONGO_URI'))
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env.local")


MONGO_URL = os.environ.get("MONGO_URL", "mongo")
MONGO_USERNAME = os.environ.get("MONGO_USENAME", "root")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "")
MONGO_PORT = os.environ.get("MONGO_PORT", 27017)

mongo_client = MongoClient(
    host=MONGO_URL, username=MONGO_USERNAME, password=MONGO_PASSWORD, port=MONGO_PORT
)


def insert_test_document():
    db = mongo_client.test
    test_colllecttion = db.test_collection
    res = test_colllecttion.insert_one({"name": "Bogdan", "instructor": True})
    print(res)

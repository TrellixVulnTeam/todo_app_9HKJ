import datetime
from pymongo import MongoClient

class Model():
    client = MongoClient()
    db = client['todoDB']
    todos = db['todos']
    users = db['users']
    def __init__(self):pass


import datetime
from model import Model


class Collection(Model):
    
    def __init__(self):
        pass

    def index(self):pass

    def add(self):
        collection = {"author": "Mike", "date": datetime.datetime.utcnow()}
        collection_id = self.todos.insert_one(collection).inserted_id
        return str(collection_id)

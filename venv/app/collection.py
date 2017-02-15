import json
import pprint

from datetime import datetime
from bson import Binary, Code
from bson.json_util import dumps
from bson.json_util import loads

from flask import session, redirect, url_for

from model import Model

class Collection(Model):
    def __init__(self):
        super().__init__()

    def index(self):
        pass

    def add(self, request):
        coll = request.form['collection']
        email = session['user']['email']

        # Check if this user email already exists
        data = self.todos.find({"user.email": email})

        for record in data:
            if record['collection']['label'] == coll: return redirect(url_for("add_collection"))

        result = self.todos.update({"user.email": email},
                                   {"$push": {"collection": {"$each": [{"label": coll, "cards": []}]}}})
        if result:
            return redirect(url_for("dashboard"))
        return redirect(url_for("add_collection"))
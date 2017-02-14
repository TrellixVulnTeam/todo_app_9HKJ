from flask import Flask
from collection import Collection

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Tanzania"


@app.route("/dashboard")
def dashboard():
    return "Welcome to dashboard"

# --------------------------------------------------------
#Definition of User Class routes
#------------------------------------------------------

@app.route("/users/register")
def register_user():
    return "Registering new user"

@app.route("/users/login")
def edit_user():
    return "Login to account"

@app.route("/users/edit/<int:user_id>")
def edit_user(user_id):
    return "Editing user profile"

# --------------------------------------------------------
#Definition of Collection Class routes
#------------------------------------------------------
@app.route("/collection")
def collection():
    return "Available collections"

@app.route("/collection/add")
def add_collection():
    coll = Collection()
    return coll.add()

@app.route("/collection/edit/<int:id>")
def edit_collection(id):
    return "Edit collection %d" % id

@app.route("/collection/view/<int:id>")
def view_collection(id):
    return "View collection %d" % id

@app.route("/collection/delete/<int:id>")
def delete_collection(id):
    return "Delete collection %d" % id

# --------------------------------------------------------
#Definition of Card Class routes
#------------------------------------------------------
@app.route("/cards")
def card():
    return "All Cards available"

@app.route("/cards/add")
def add_card():
    return "You are adding a card"


@app.route("/cards/edit/<int:id>")
def edit_card(id):
    return "You are editing a card %d" % id


@app.route("/cards/view/<int:id>")
def view_card(id):
    return "You are Viewing a card %d" % id


@app.route("/cards/delete/<int:id>")
def delete_card(id):
    return "You are deleting a card %d" % id

@app.route("/cards/move/<int:collection_id>/<int:card_id>")
def move_card(collection_id, card_id):
    return "You are Moving Card " + str(card_id) + " to Collection " + str(collection_id)


@app.route("/cards/item/<int:card_id>")
def undo_card(card_id):
    return "You have undone the changes for card %d" % card_id

@app.route("/cards/undo/<int:card_id>")
def undo_card(card_id):
    return "You have undone the changes for card %d" % card_id

if __name__ == "__main__":
    app.run(debug=True)
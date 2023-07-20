from flask import Flask
from auth import validate
from user import list_user, create_user, existing_user

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user")
def user():
    list_of_user = list_user()
    return list_of_user

@app.route("/register/<user>/<password>")
def register(user, password):
    if not existing_user(user):
        create_user(user, password)
        return f"Successfully created user {user}", 201
    else:
        return f"User {user} already exist", 200
    
    

@app.route("/login/<user>/<password>")
def login(user, password):
    response = f"User {user} is {'' if validate(user, password) else 'not '} valid."
    return response
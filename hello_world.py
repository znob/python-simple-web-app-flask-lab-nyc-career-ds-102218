# import flask here
from flask import Flask

# create new Flask App here
app = Flask(__name__)

# define routes for your new flask app
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/home')
def index():
    return "Welcome to an amazing Flask App!"

@app.route('/myprofile')
def index():
    return "This is my profile! It's not finished yet... :/"

@app.route('/exit')
def index():
    return  "Thanks for looking around. Come back again soon!"

# tell your flask app to run with debug mode on
app.run(debug=True)

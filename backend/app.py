from flask import Flask
from db.connection import SessionLocal
from db.models import *


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello_world():
    print("Hello, World!")
    return "<p>Hello, World!</p>"



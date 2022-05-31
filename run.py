from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)

    
@app.route("/", methods=["GET"])
def hello_world():
    return 'Ola, estou na aplicação setad'



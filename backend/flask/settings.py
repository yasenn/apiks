#!/usr/bin/env python3

from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_restful_swagger import swagger

app = Flask(__name__)

# Wrap the Api with swagger.docs. It is a thin wrapper around the Api class that adds some swagger smarts
api = swagger.docs(Api(app), apiVersion='0.1')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db
app.config['SQLALCHEMY_TRACK_MODFICATIONS'] = False

@app.route("/")
def hello():
    return "Hello, World!"

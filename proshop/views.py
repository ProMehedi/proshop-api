from flask import jsonify
from flask_restful import Resource
from .config import db


class Hello(Resource):
    def get(self):
        return jsonify({'hello': 'Hey, I am a Flask RESTful API', "name": "Mehedi Hasan", "github": "https://github.com/proMehedi/proshop-api"})


class User(Resource):
    def post(self):
        users = db['users']
        users.insert_one({"name": "Mehedi Hasan"})
        return jsonify({"user": "user created successfully"})

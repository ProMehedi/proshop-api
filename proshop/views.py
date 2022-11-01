from flask_restful import Resource


class Hello(Resource):
    def get(self):
        return {'hello': 'Hey, I am a Flask RESTful API', "name": "Mehedi Hasan", "github": "https://github.com/proMehedi/proshop-api"}


class User(Resource):
    def post(self):
        return {'user': 'user'}

from flask import Flask
from flask_restful import Api


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    api = Api(app)

    from .views import Hello, User

    api.add_resource(Hello, '/')
    api.add_resource(User, '/user')

    return app

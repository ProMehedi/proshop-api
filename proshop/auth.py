from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.get('/')
def index():
    return 'Auth'

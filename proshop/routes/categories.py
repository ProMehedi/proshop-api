from flask import Blueprint

categories = Blueprint('categories', __name__)


@categories.get('/')
def index():
    return 'categories'

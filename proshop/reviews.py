from flask import Blueprint

reviews = Blueprint('reviews', __name__)


@reviews.get('/')
def index():
    return 'reviews'

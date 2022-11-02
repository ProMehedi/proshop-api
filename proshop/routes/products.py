from flask import Blueprint

products = Blueprint('products', __name__)


@products.get('/')
def index():
    return 'Products'

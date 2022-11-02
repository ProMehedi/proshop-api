from flask import Blueprint

orders = Blueprint('orders', __name__)


@orders.get('/')
def index():
    return 'orders'

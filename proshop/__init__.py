from flask import Flask
from .settings import URL_PREFIX


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    from .auth import auth
    from .products import products
    from .orders import orders
    from .categories import categories
    from .reviews import reviews

    app.register_blueprint(auth, url_prefix=f'/{URL_PREFIX}/auth')
    app.register_blueprint(products, url_prefix=f'/{URL_PREFIX}/products')
    app.register_blueprint(orders, url_prefix=f'/{URL_PREFIX}/orders')
    app.register_blueprint(categories, url_prefix=f'/{URL_PREFIX}/categories')
    app.register_blueprint(reviews, url_prefix=f'/{URL_PREFIX}/reviews')

    return app

from flask import Flask
from .configs.settings import URL_PREFIX


def create_app(config_file='configs/settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    from .routes.user import user
    from .routes.products import products
    from .routes.orders import orders
    from .routes.categories import categories
    from .routes.reviews import reviews

    app.register_blueprint(user, url_prefix=f'/{URL_PREFIX}/user')
    app.register_blueprint(products, url_prefix=f'/{URL_PREFIX}/products')
    app.register_blueprint(orders, url_prefix=f'/{URL_PREFIX}/orders')
    app.register_blueprint(categories, url_prefix=f'/{URL_PREFIX}/categories')
    app.register_blueprint(reviews, url_prefix=f'/{URL_PREFIX}/reviews')

    return app

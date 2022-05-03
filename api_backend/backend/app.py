from flask import Flask

from backend.customers import customers
from backend.products import products
from backend.reviews import reviews
from backend.config import configure_app_dev
from backend.cassandra import cs


def init_app():
    app = Flask(__name__)

    # load config
    configure_app_dev(app)

    # init services
    cs.init_app(app)

    # register blueprints
    app.register_blueprint(customers)
    app.register_blueprint(products)
    app.register_blueprint(reviews)

    @app.route("/")
    @app.route("/_health")
    def health():
        return "OK!"

    return app


app = init_app()

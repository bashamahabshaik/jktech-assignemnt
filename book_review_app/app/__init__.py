from flask import Flask
from app.config import Config
# from app.db import db
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # db.init_app(app)

    from app.routes import book_routes, review_routes, summary_routes
    app.register_blueprint(book_routes.bp)
    app.register_blueprint(review_routes.bp)
    app.register_blueprint(summary_routes.bp)

    return app

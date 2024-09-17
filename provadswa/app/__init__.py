from flask import Flask
from config import Config
from .models import db
from flask_bootstrap import Bootstrap
from flask_moment import Moment


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)
    moment = Moment(app)


    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

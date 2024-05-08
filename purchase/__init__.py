import os
import click
import json

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from purchase.models import db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'purchase.sqlite'),
    # )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myodoo:12345678@localhost/flask_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

    # Import models
    # import purchase.models

    # Initialize SQLAlchemy
    db.init_app(app)

    
    # Create tables
    with app.app_context():
        db.create_all()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/") 
    def index(): 
        return render_template('main_menu.html')

    # from . import db
    # db.init_app(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import auth
    app.register_blueprint(auth.bp)

    from . import purchase
    app.register_blueprint(purchase.bp)

    from . import migration
    app.register_blueprint(migration.bp)

    return app
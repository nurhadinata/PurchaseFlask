import os
import click
import json

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from purchase.models import ResUserOdoo, ProductOdoo, PurchaseOrderOdoo, PurchaseOrderLineOdoo, NfcappFarmerOdoo, PurchaseEvent, Transaction
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

    @app.route('/selectpickerUser', methods=["GET"])
    def selectpickerUser():
        query = request.args.get('q')

        user_list = ResUserOdoo.query.filter(ResUserOdoo.login.ilike(f'%{query}%')).all()

        res_user = [{
            "id": user.id,
            "text": user.login,
        } for user in user_list]

        # res_users.append({
        #     "id": "all",
        #     "text": "All",
        # })

        return json.dumps(res_user)

    @app.route('/selectpickerPo', methods=["GET"])
    def selectpickerPo():
        query = request.args.get('q')

        po_list = PurchaseOrderOdoo.query.filter(PurchaseOrderOdoo.name.ilike(f'%{query}%')).order_by(PurchaseOrderOdoo.id.desc()).all()

        res_po = [{
            "id": po.id,
            "text": po.name,
        } for po in po_list]

        # res_users.append({
        #     "id": "all",
        #     "text": "All",
        # })

        return json.dumps(res_po)

    @app.route('/selectpickerPurchaseEvent', methods=["GET"])
    def selectpickerPurchaseEvent():
        query = request.args.get('q')

        event_list = PurchaseEvent.query.filter(PurchaseEvent.name.ilike(f'%{query}%')).order_by(PurchaseEvent.id.desc()).all()

        res_event = [{
            "id": event.id,
            "text": event.name,
        } for event in event_list]

        # res_users.append({
        #     "id": "all",
        #     "text": "All",
        # })

        return json.dumps(res_event)

    @app.route('/selectpickerFarmer', methods=["GET"])
    def selectpickerFarmer():
        query = request.args.get('q')

        farmer_list = NfcappFarmerOdoo.query.filter(NfcappFarmerOdoo.farmer_name.ilike(f'%{query}%')).order_by(NfcappFarmerOdoo.farmer_name).all()

        res_farmer = [{
            "id": farmer.id,
            "text": farmer.farmer_name,
        } for farmer in farmer_list]

        # res_users.append({
        #     "id": "all",
        #     "text": "All",
        # })

        return json.dumps(res_farmer)

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
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask import jsonify
from purchase.models import db
from werkzeug.security import check_password_hash, generate_password_hash
from purchase.models import ResUserOdoo, ProductOdoo, PurchaseOrderOdoo, PurchaseOrderLineOdoo, NfcappFarmerOdoo, PurchaseEvent

bp = Blueprint('purchase', __name__, url_prefix='/purchase')

@bp.route('/report', methods=["GET"])
def purchase_report():
    return render_template('purchase/report.html')

@bp.route('/list', methods=["GET"])
def purchase_list():
    return render_template('purchase/list.html')

@bp.route('/farmer-list', methods=["GET"])
def farmer_list():
    farmers = NfcappFarmerOdoo.query.all()
    return render_template('purchase/farmer_list.html', farmers=farmers)

@bp.route('/event', methods=["GET"])
def event_list():
    users = ResUserOdoo.query.all()
    events = PurchaseEvent.query.order_by(PurchaseEvent.id).all()
    return render_template('purchase/event.html', events=events, users=users)

@bp.route('/event/add', methods=["POST"])
def event_add():

    fund = request.form['fund']
    purchaser = request.form['purchaser']
    cashier = request.form['cashier']
        
    
    purchase_event = PurchaseEvent(fund=fund, purchaser=purchaser, cashier=cashier)
    db.session.add(purchase_event)
    db.session.commit()

    return redirect(url_for('purchase.event_list'))

@bp.route('/event/update', methods=["POST"])
def event_update():
    # Retrieve updated data from the POST request
    updated_data = request.json
    
    # Update the data dictionary
    event = PurchaseEvent.query.filter_by(id=updated_data.get('id')).first()  # Example: Update the user with ID 1
    if event:
        event.fund = updated_data.get('fund', event.fund)
        event.purchaser = updated_data.get('purchaser', event.purchaser)
        event.cashier = updated_data.get('cashier', event.cashier)
        db.session.commit()
        return jsonify({'message': 'Data updated successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404
    
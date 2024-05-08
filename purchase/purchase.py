import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from purchase.models import ResUserOdoo, ProductOdoo, PurchaseOrderOdoo, PurchaseOrderLineOdoo, NfcappFarmerOdoo

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
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
session = db.session

class User2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class ProductOdoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    default_code = db.Column(db.String)
    active = db.Column(db.Boolean)
    product_tmpl_id = db.Column(db.Integer)
    barcode = db.Column(db.String)
    combination_indices = db.Column(db.String)
    volume = db.Column(db.Numeric)
    weight = db.Column(db.Numeric)
    can_image_variant_1024_be_zoomed = db.Column(db.Boolean)
    message_main_attachment_id = db.Column(db.Integer)
    create_uid = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    write_uid = db.Column(db.Integer)
    write_date = db.Column(db.DateTime)
    gross_weight = db.Column(db.Numeric)
    pack_uom_id = db.Column(db.Integer)
    is_pallet = db.Column(db.Boolean)
    sub_category = db.Column(db.String)
    substance = db.Column(db.String)
    master_code = db.Column(db.String)
    sub_commodity = db.Column(db.String)
    commodity = db.Column(db.String)
    person_in_charge = db.Column(db.String)
    qty_pallet = db.Column(db.Numeric)
    uom_char = db.Column(db.String)
    cost_uom = db.Column(db.String)
    conversion_cost_uom = db.Column(db.Float)
    cost_bom_id = db.Column(db.Integer)
    cost_price_currency = db.Column(db.Float)
    cost_currency_id = db.Column(db.Integer)
    x_color = db.Column(db.String)
    cost_bom_id2 = db.Column(db.Integer)
    cost_price_currency2 = db.Column(db.Float)
    packaging_set_id = db.Column(db.Integer)
    foh_product_id = db.Column(db.Integer)
    percent_shrinkage = db.Column(db.Float)
    cost_bom_id3 = db.Column(db.Integer)
    cost_bom_id4 = db.Column(db.Integer)
    cost_price_currency4 = db.Column(db.Float)

    def __repr__(self):
        return f'<ProductOdoo {self.default_code}>'

class NfcappFarmerOdoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer)
    code = db.Column(db.String)
    farmer_name = db.Column(db.String)
    farmer_role = db.Column(db.String)
    certification_status_id = db.Column(db.Integer)
    certification_date = db.Column(db.Date)
    first_year_organic = db.Column(db.Integer)
    first_year_fl = db.Column(db.Integer)
    first_year_ra = db.Column(db.Integer)
    first_cert_ra = db.Column(db.Date)
    last_cert_ra = db.Column(db.Date)
    registration_date = db.Column(db.Date)
    contract_date = db.Column(db.Date)
    gender = db.Column(db.String)
    date_of_birth = db.Column(db.Date)
    phone_number = db.Column(db.String)
    household_size = db.Column(db.Float)
    number_of_worker = db.Column(db.Integer)
    status_of_worker = db.Column(db.String)
    bank_name_id = db.Column(db.Integer)
    bank_holder = db.Column(db.String)
    bank_akun = db.Column(db.String)
    document_is_digital = db.Column(db.Boolean)
    puid = db.Column(db.String)
    note = db.Column(db.Text)
    active = db.Column(db.Boolean)
    no_ktp = db.Column(db.String)
    custom_document_char = db.Column(db.String)
    custom_photo_char = db.Column(db.String)
    custom_ktp_photo_char = db.Column(db.String)
    create_uid = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    write_uid = db.Column(db.Integer)
    write_date = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Farmer {self.farmer_name}>'

class PurchaseOrderOdoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_main_attachment_id = db.Column(db.Integer)
    access_token = db.Column(db.String)
    name = db.Column(db.String)
    origin = db.Column(db.String)
    partner_ref = db.Column(db.String)
    date_order = db.Column(db.DateTime)
    date_approve = db.Column(db.DateTime)
    partner_id = db.Column(db.Integer)
    dest_address_id = db.Column(db.Integer)
    currency_id = db.Column(db.Integer)
    state = db.Column(db.String)
    notes = db.Column(db.Text)
    invoice_count = db.Column(db.Integer)
    invoice_status = db.Column(db.String)
    date_planned = db.Column(db.DateTime)
    amount_untaxed = db.Column(db.Numeric)
    amount_tax = db.Column(db.Numeric)
    amount_total = db.Column(db.Numeric)
    fiscal_position_id = db.Column(db.Integer)
    payment_term_id = db.Column(db.Integer)
    incoterm_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    company_id = db.Column(db.Integer)
    currency_rate = db.Column(db.Float)
    create_uid = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    write_uid = db.Column(db.Integer)
    write_date = db.Column(db.DateTime)
    picking_count = db.Column(db.Integer)
    picking_type_id = db.Column(db.Integer)
    group_id = db.Column(db.Integer)
    auto_generated = db.Column(db.Boolean)
    auto_sale_order_id = db.Column(db.Integer)
    analytic_account_id = db.Column(db.Integer)
    interco_po = db.Column(db.Integer)
    requisition_id = db.Column(db.Integer)

    def __repr__(self):
        return f'<PurchaseOrderOdoo {self.name}>'

class PurchaseOrderLineOdoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    sequence = db.Column(db.Integer)
    product_qty = db.Column(db.Numeric)
    product_uom_qty = db.Column(db.Float)
    date_planned = db.Column(db.DateTime)
    product_uom = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    price_unit = db.Column(db.Numeric)
    price_subtotal = db.Column(db.Numeric)
    price_total = db.Column(db.Numeric)
    price_tax = db.Column(db.Float)
    order_id = db.Column(db.Integer)
    account_analytic_id = db.Column(db.Integer)
    company_id = db.Column(db.Integer)
    state = db.Column(db.String)
    qty_invoiced = db.Column(db.Numeric)
    qty_received_method = db.Column(db.String)
    qty_received = db.Column(db.Numeric)
    qty_received_manual = db.Column(db.Numeric)
    partner_id = db.Column(db.Integer)
    currency_id = db.Column(db.Integer)
    display_type = db.Column(db.String)
    create_uid = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    write_uid = db.Column(db.Integer)
    write_date = db.Column(db.DateTime)
    orderpoint_id = db.Column(db.Integer)
    propagate_date = db.Column(db.Boolean)
    propagate_date_minimum_delta = db.Column(db.Integer)
    propagate_cancel = db.Column(db.Boolean)
    sale_order_id = db.Column(db.Integer)
    sale_line_id = db.Column(db.Integer)
    is_deposit = db.Column(db.Boolean)
    open_subtotal = db.Column(db.Float)

    def __repr__(self):
        return f'<PurchaseOrderLineOdoo {self.name}>'

class ResUserOdoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, default=True)
    login = db.Column(db.String)
    password = db.Column(db.String)
    company_id = db.Column(db.Integer)
    partner_id = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    signature = db.Column(db.Text)
    action_id = db.Column(db.Integer)
    share = db.Column(db.Boolean)
    create_uid = db.Column(db.Integer)
    write_uid = db.Column(db.Integer)
    write_date = db.Column(db.DateTime)
    alias_id = db.Column(db.Integer)
    notification_type = db.Column(db.String)
    out_of_office_message = db.Column(db.String)
    karma = db.Column(db.Integer)
    rank_id = db.Column(db.Integer)
    next_rank_id = db.Column(db.Integer)
    odoobot_state = db.Column(db.String)
    sale_team_id = db.Column(db.Integer)
    website_id = db.Column(db.Integer)
    target_sales_won = db.Column(db.Integer)
    target_sales_done = db.Column(db.Integer)
    target_sales_invoiced = db.Column(db.Integer)
    password_write_date = db.Column(db.DateTime)

    # # Define unique constraint for login and website_id
    # __table_args__ = (
    #     db.UniqueConstraint('login', 'website_id', name='res_users_login_website_key'),
    # )


class PurchaseEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    fund = db.Column(db.Float, default=100000)
    ics = db.Column(db.String)
    purchaser_id = db.Column(db.Integer, db.ForeignKey('res_user_odoo.id'))
    purchaser = db.relationship('ResUserOdoo', foreign_keys=[purchaser_id], backref=db.backref('purchaser_events', lazy=True))
    cashier_id = db.Column(db.Integer, db.ForeignKey('res_user_odoo.id'))
    cashier = db.relationship('ResUserOdoo', foreign_keys=[cashier_id], backref=db.backref('cashier_events', lazy=True))
    ap_name = db.Column(db.String)
    ip_address = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, fund, purchaser_id, cashier_id):
        self.fund = fund
        self.purchaser_id = purchaser_id
        self.cashier_id = cashier_id
        self.ip_address = request.remote_addr
        self.created_at = datetime.utcnow()
        self.generate_name()

    def generate_name(self):
        # Get current date in the format YYYYMMDD
        date_str = self.created_at.strftime('%Y%m%d')
        # Count existing posts for the current date
        post_count = PurchaseEvent.query.filter(PurchaseEvent.created_at >= datetime.combine(self.created_at.date(), datetime.min.time())).count()
        # Set the name using the format PE-date-index
        self.name = f"PE{date_str}-{post_count + 1}"

    def __repr__(self):
        return f'<PurchaseEvent {self.purchase_event}>'

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purchase_order_id = db.Column(db.Integer, db.ForeignKey('purchase_order_odoo.id'))
    purchase_order = db.relationship('PurchaseOrderOdoo', foreign_keys=[purchase_order_id], backref=db.backref('transactions', lazy=True))
    station = db.Column(db.String, default="default")
    purchase_event_id = db.Column(db.Integer, db.ForeignKey('purchase_event.id'))
    purchase_event = db.relationship('PurchaseEvent', foreign_keys=[purchase_event_id], backref=db.backref('transactions', lazy=True))
    farmer_id = db.Column(db.Integer, db.ForeignKey('nfcapp_farmer_odoo.id'))
    farmer = db.relationship('NfcappFarmerOdoo', foreign_keys=[farmer_id], backref=db.backref('transactions', lazy=True))
    # item_code_id = db.Column(db.Integer, db.ForeignKey('product_odoo.id'))
    # item_code = db.Column(db.Integer, db.ForeignKey('product_odoo.id'))
    price_unit = db.Column(db.Float, default=100000)
    qty = db.Column(db.Float, default=100)
    subtotal = db.Column(db.Float)

    def __init__(self, purchase_order_id, purchase_event_id, farmer_id, price_unit, qty):
        self.purchase_order_id = purchase_order_id
        self.purchase_event_id = purchase_event_id
        self.farmer_id = farmer_id
        self.price_unit = price_unit
        self.qty =  qty
        self.subtotal = price_unit * qty

    def __repr__(self):
        return f'<Transaction {self.id}>'










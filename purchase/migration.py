import functools

import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flask_sqlalchemy import SQLAlchemy
from purchase.models import db, ResUserOdoo, ProductOdoo, PurchaseOrderOdoo, PurchaseOrderLineOdoo, NfcappFarmerOdoo, session


bp = Blueprint('migration', __name__, url_prefix='/migrate')

import xmlrpc.client
from purchase.config import ODOO_URL, ODOO_DB, ODOO_PASSWORD, ODOO_USERNAME

# url = 'http://localhost:8069'
# odoo_db = 'tripperDB'
# username = 'cerdas@tripper.com'
# password = 'Cerdas@2024'

    


@bp.route('/sync_with_odoo')
def sync_with_odoo():
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(ODOO_URL))
    uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(ODOO_URL))

    # Call the method exposed in Odoo
    data = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'external.service', 'get_data', ["res_users"])

    flask_data = ResUserOdoo.query.all()

    # Convert existing data to a dictionary for easier comparison
    flask_data_dict = {record.id: record for record in flask_data}
        

    for record in data:
        for key, value in record.items():
            if value == 'none':
                record[key] = None
        record_id = record.get('id')
        flask_record = flask_data_dict.get(record_id)
        
        if flask_record:
            # Update the existing record with data from Odoo
            for key, value in record.items():
                setattr(flask_record, key, value)
        # If the record does not exist in the Flask database, insert it as a new record
        elif not flask_record:
            new_record = ResUserOdoo(**record)
            db.session.add(new_record)

    # Commit changes to the database
    db.session.commit()

    # common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(ODOO_URL))
    # uid = common.authenticate(ODOO_DB, username, password, {})
    # models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(ODOO_URL))

    # Call the method exposed in Odoo
    odoo_table = "product_product"
    data = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'external.service', 'get_data', [odoo_table])

    flask_table = ProductOdoo
    flask_data = flask_table.query.all()

    # Convert existing data to a dictionary for easier comparison
    flask_data_dict = {record.id: record for record in flask_data}
        

    for record in data:
        for key, value in record.items():
            if value == 'none':
                record[key] = None
        record_id = record.get('id')
        flask_record = flask_data_dict.get(record_id)
    
        # If the record exists in the Flask database and it's different from the one in Odoo
        if flask_record:
            # Update the existing record with data from Odoo
            for key, value in record.items():
                setattr(flask_record, key, value)
        # If the record does not exist in the Flask database, insert it as a new record
        elif not flask_record:
            new_record = flask_table(**record)
            db.session.add(new_record)

    # Commit changes to the database
    db.session.commit()

    # common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(ODOO_URL))
    # uid = common.authenticate(ODOO_DB, username, password, {})
    # models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(ODOO_URL))

    # Call the method exposed in Odoo
    odoo_table = "purchase_order"
    data = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'external.service', 'get_data', [odoo_table])

    flask_table = PurchaseOrderOdoo
    flask_data = flask_table.query.all()

    # Convert existing data to a dictionary for easier comparison
    flask_data_dict = {record.id: record for record in flask_data}
        

    for record in data:
        for key, value in record.items():
            if value == 'none':
                record[key] = None
        
        record_id = record.get('id')
        flask_record = flask_data_dict.get(record_id)
        
        # If the record exists in the Flask database and it's different from the one in Odoo
        if flask_record:
            # Update the existing record with data from Odoo
            for key, value in record.items():
                setattr(flask_record, key, value)
            # Add the record to the session for tracking changes
    
        # If the record does not exist in the Flask database, insert it as a new record
        elif not flask_record:
            new_record = flask_table(**record)
            db.session.add(new_record)

    # Commit changes to the database
    db.session.commit()

    # common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    # uid = common.authenticate(ODOO_DB, username, ODOO_PASSWORD, {})
    # models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    # # Call the method exposed in Odoo
    # odoo_table = "purchase_order_line"
    # data = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'external.service', 'get_data', [odoo_table])

    # flask_table = PurchaseOrderLineOdoo
    # flask_data = flask_table.query.all()

    # # Convert existing data to a dictionary for easier comparison
    # flask_data_dict = {record.id: record for record in flask_data}
        

    # for record in data:
    #     for key, value in record.items():
    #         if value == 'none':
    #             record[key] = None

    #     record_id = record.get('id')
    #     flask_record = flask_data_dict.get(record_id)
    #     # instance = ResUserOdoo(**record)

    #     # print(db)
        
    #     # # Add the instance to the session
    #     # db.session.add(instance)
    #     # If the record exists in the Flask database and it's different from the one in Odoo
    #     if flask_record:
    #         # Update the existing record with data from Odoo
    #         # flask_record.__dict__.update(record)
    #         for key, value in record.items():
    #             setattr(flask_record, key, value)
    #         # Add the record to the session for tracking changes
    #         # db.session.add(flask_record)
    #     # If the record does not exist in the Flask database, insert it as a new record
    #     elif not flask_record:
    #         new_record = flask_table(**record)
    #         db.session.add(new_record)

    # # Commit changes to the database
    # db.session.commit()
        
    # common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(ODOO_URL))
    # uid = common.authenticate(ODOO_DB, username, ODOO_PASSWORD, {})
    # models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(ODOO_URL))

    # Call the method exposed in Odoo
    odoo_table = "nfcapp_farmer"
    data = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'external.service', 'get_data', [odoo_table])

    flask_table = NfcappFarmerOdoo
    flask_data = flask_table.query.all()

    # Convert existing data to a dictionary for easier comparison
    flask_data_dict = {record.id: record for record in flask_data}
        

    for record in data:
        for key, value in record.items():
            if value == 'none':
                record[key] = None
        
        record_id = record.get('id')
        flask_record = flask_data_dict.get(record_id)
        
        # If the record exists in the Flask database and it's different from the one in Odoo
        if flask_record:
            # Update the existing record with data from Odoo
            for key, value in record.items():
                setattr(flask_record, key, value)
            # Add the record to the session for tracking changes

        # If the record does not exist in the Flask database, insert it as a new record
        elif not flask_record:
            new_record = flask_table(**record)
            db.session.add(new_record)

    # Commit changes to the database
    db.session.commit()
        
        
    return 'Data updated successfully'

@bp.route('/sync_res_user')
def sync_res_user():
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(ODOO_URL))
    uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(ODOO_URL))

    # Call the method exposed in Odoo
    data = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'external.service', 'get_data', ["res_users"])

    flask_data = ResUserOdoo.query.all()

    # Convert existing data to a dictionary for easier comparison
    flask_data_dict = {record.id: record for record in flask_data}
        

    for record in data:
        for key, value in record.items():
            if value == 'none':
                record[key] = None
        
        record_id = record.get('id')
        flask_record = flask_data_dict.get(record_id)
        
        # If the record exists in the Flask database and it's different from the one in Odoo
        if flask_record:
            # Update the existing record with data from Odoo
            for key, value in record.items():
                setattr(flask_record, key, value)
            # Add the record to the session for tracking changes

        # If the record does not exist in the Flask database, insert it as a new record
        elif not flask_record:
            new_record = ResUserOdoo(**record)
            db.session.add(new_record)

    # Commit changes to the database
    db.session.commit()        
        
    return 'ResUserOdoo updated successfully'

@bp.route('/migrate_res_user')
def migrate_res_user():
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(ODOO_URL))
    uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(ODOO_URL))

    # Call the method exposed in Odoo
    odoo_data = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'external.service', 'get_data', ["res_users"])

    flask_data = ResUserOdoo.query.all()

    # Convert existing data to a dictionary for easier comparison
    flask_data_dict = [vars(item) for item in flask_data]
    # flask_data_dict = {record.id: record for record in flask_data}
        

    for record in flask_data_dict:
        record.pop('_sa_instance_state', None)
        record_id = record.get('id')
        odoo_record = None
        for item in odoo_data:
            if item.get('id') == record_id:
                odoo_record = item

        for key, value in record.items():
            if value == None:
                record[key] = 'None'
        
        # If the record exists in the Flask database and it's different from the one in Odoo
        if odoo_record:
            print(sorted(record.items()))
            print(sorted(odoo_record.items()))
            print(sorted(record.items())==sorted(odoo_record.items()))
            
            # Check if the two lists are equal
            equal = all(normalize_value(v1) == normalize_value(v2) for (k1, v1), (k2, v2) in zip(sorted(record.items()), sorted(odoo_record.items())))
            if not equal:
                # If the record exists in the Odoo database, update it with the data from Odoo
                models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'external.service', 'update_data', ["res.user", record_id, record])
                # Additionally, consider handling the case where the update operation fails
                

        elif not odoo_record:
            # If the record does not exist in the Odoo database, insert it as a new record
            models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'res.users', 'create', [record])
            # Consider implementing error handling for the creation operation as well


    # Commit changes to the database
    db.session.commit()        
        
    return 'ResUserOdoo updated successfully'

@bp.route('/sync_product_odoo')
def sync_product_odoo():
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(ODOO_URL))
    uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(ODOO_URL))

    # Call the method exposed in Odoo
    odoo_table = "product_product"
    data = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'external.service', 'get_data', [odoo_table])

    flask_table = ProductOdoo
    flask_data = flask_table.query.all()

    # Convert existing data to a dictionary for easier comparison
    flask_data_dict = {record.id: record for record in flask_data}
        

    for record in data:
        for key, value in record.items():
            if value == 'none':
                record[key] = None
        
        record_id = record.get('id')
        flask_record = flask_data_dict.get(record_id)
        
        # If the record exists in the Flask database and it's different from the one in Odoo
        if flask_record:
            # Update the existing record with data from Odoo
            for key, value in record.items():
                setattr(flask_record, key, value)
            # Add the record to the session for tracking changes

        # If the record does not exist in the Flask database, insert it as a new record
        elif not flask_record:
            new_record = flask_table(**record)
            db.session.add(new_record)

    # Commit changes to the database
    db.session.commit()
        
    return 'ProductOdoo updated successfully'

@bp.route('/sync_purchase_order_odoo')
def sync_purchase_order_odoo():
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(ODOO_URL))
    uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(ODOO_URL))

    # Call the method exposed in Odoo
    odoo_table = "purchase_order"
    data = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'external.service', 'get_data', [odoo_table])

    flask_table = PurchaseOrderOdoo
    flask_data = flask_table.query.all()

    # Convert existing data to a dictionary for easier comparison
    flask_data_dict = {record.id: record for record in flask_data}
        

    for record in data:
        for key, value in record.items():
            if value == 'none':
                record[key] = None
        
        record_id = record.get('id')
        flask_record = flask_data_dict.get(record_id)
        
        # If the record exists in the Flask database and it's different from the one in Odoo
        if flask_record:
            # Update the existing record with data from Odoo
            for key, value in record.items():
                setattr(flask_record, key, value)
            # Add the record to the session for tracking changes

        # If the record does not exist in the Flask database, insert it as a new record
        elif not flask_record:
            new_record = flask_table(**record)
            db.session.add(new_record)

    # Commit changes to the database
    db.session.commit()
        
    return 'PurchaseOrderOdoo updated successfully'

@bp.route('/sync_purchase_order_line_odoo')
def sync_purchase_order_line_odoo():
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(ODOO_URL))
    uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(ODOO_URL))

    # Call the method exposed in Odoo
    odoo_table = "purchase_order_line"
    data = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'external.service', 'get_data', [odoo_table])

    flask_table = PurchaseOrderLineOdoo
    flask_data = flask_table.query.all()

    # Convert existing data to a dictionary for easier comparison
    flask_data_dict = {record.id: record for record in flask_data}
        

    for record in data:
        for key, value in record.items():
            if value == 'none':
                record[key] = None
        
        record_id = record.get('id')
        flask_record = flask_data_dict.get(record_id)
        
        # If the record exists in the Flask database and it's different from the one in Odoo
        if flask_record:
            # Update the existing record with data from Odoo
            for key, value in record.items():
                setattr(flask_record, key, value)
            # Add the record to the session for tracking changes

        # If the record does not exist in the Flask database, insert it as a new record
        elif not flask_record:
            new_record = flask_table(**record)
            db.session.add(new_record)

    # Commit changes to the database
    db.session.commit()
        
    return 'PurchaseOrderLineOdoo updated successfully'

@bp.route('/sync_farmer_odoo')
def sync_farmer_odoo():
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(ODOO_URL))
    uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(ODOO_URL))

    # Call the method exposed in Odoo
    odoo_table = "nfcapp_farmer"
    data = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'external.service', 'get_data', [odoo_table])

    flask_table = NfcappFarmerOdoo
    flask_data = flask_table.query.all()

    # Convert existing data to a dictionary for easier comparison
    flask_data_dict = {record.id: record for record in flask_data}
        

    for record in data:
        for key, value in record.items():
            if value == 'none':
                record[key] = None
        
        record_id = record.get('id')
        flask_record = flask_data_dict.get(record_id)
        
        # If the record exists in the Flask database and it's different from the one in Odoo
        if flask_record:
            # Update the existing record with data from Odoo
            for key, value in record.items():
                setattr(flask_record, key, value)
            # Add the record to the session for tracking changes

        # If the record does not exist in the Flask database, insert it as a new record
        elif not flask_record:
            new_record = flask_table(**record)
            db.session.add(new_record)

    # Commit changes to the database
    db.session.commit()
        
    return 'NfcappFarmerOdoo updated successfully'

def normalize_value(value):
    if isinstance(value, str):
        return value.lower() if value.lower() != 'none' else None
    elif isinstance(value, datetime.datetime):
        return value.strftime('%Y-%m-%d %H:%M:%S')
    return value


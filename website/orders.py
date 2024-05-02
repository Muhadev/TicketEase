from flask import Blueprint, render_template
# from . import mysql  # Import MySQL instance

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders')
def orders(mysql):
    # Fetch data from the 'orders' table
    cur = mysql.get_db().cursor()
    cur.execute("SELECT * FROM orders")
    data = cur.fetchall()
    cur.close()
    return render_template('orders.html', orders=data)

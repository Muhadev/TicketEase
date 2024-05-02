from flask import Blueprint, render_template
# from . import mysql  # Import MySQL instance

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/payments')
def payments(mysql):
    # Fetch data from the 'payments' table
    cur = mysql.get_db().cursor()
    cur.execute("SELECT * FROM payments")
    data = cur.fetchall()
    cur.close()
    return render_template('payments.html', payments=data)

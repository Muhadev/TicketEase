from flask import Blueprint, render_template
# from . import mysql  # Import MySQL instance

tickets_bp = Blueprint('tickets', __name__)

@tickets_bp.route('/tickets')
def tickets(mysql):
    # Fetch data from the 'tickets' table
    cur = mysql.get_db().cursor()
    cur.execute("SELECT * FROM tickets")
    data = cur.fetchall()
    cur.close()
    return render_template('tickets.html', tickets=data)

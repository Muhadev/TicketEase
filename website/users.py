from flask import Blueprint, render_template
# from . import mysql  # Import MySQL instance

users_bp = Blueprint('users', __name__)

@users_bp.route('/users')
def users(mysql):
    # Fetch data from the 'users' table
    cur = mysql.get_db().cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    return render_template('users.html', users=data)

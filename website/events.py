from flask import Flask, Blueprint, render_template
# from . import mysql

events_bp = Blueprint('events', __name__)

@events_bp.route('/events')
def events(mysql):
    # Fetch data from the 'events' table
    cur = mysql.get_db().cursor()
    cur.execute("SELECT * FROM events")
    data = cur.fetchall()
    cur.close()
    return render_template('events.html', events=data)

from flask import Flask, render_template
from flaskext.mysql import MySQL

def create_app():
    app = Flask(__name__)
    
    # Configure the MySQL connection
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
    app.config['MYSQL_PASSWORD'] = 'muhammed'  # Replace with your MySQL password
    app.config['MYSQL_DB'] = 'TicketEase'  # Replace with your MySQL database name

    mysql = MySQL(app)

    # Import and register blueprints
    from .auth import auth_bp
    from .events import events_bp
    from .users import users_bp
    from .tickets import tickets_bp
    from .orders import orders_bp
    from .payments import payments_bp

    app.register_blueprint(auth_bp, url_prefix='/auth', mysql=mysql)
    app.register_blueprint(events_bp, url_prefix='/events', mysql=mysql)
    app.register_blueprint(users_bp, url_prefix='/users', mysql=mysql)
    app.register_blueprint(tickets_bp, url_prefix='/tickets', mysql=mysql)
    app.register_blueprint(orders_bp, url_prefix='/orders', mysql=mysql)
    app.register_blueprint(payments_bp, url_prefix='/payments', mysql=mysql)


    return app, mysql

# if __name__ == '__main__':
#     create_app().run(host='0.0.0.0', port=5000, debug=True)

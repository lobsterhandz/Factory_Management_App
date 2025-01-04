from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from limiter import limiter  # Import global limiter from limiter.py

# Import blueprints
from blueprints.employee_blueprint import employee_bp
from blueprints.product_blueprint import product_bp
from blueprints.order_blueprint import order_bp
from blueprints.customer_blueprint import customer_bp
from blueprints.production_blueprint import production_bp

# Initialize database
db = SQLAlchemy()

# Create Flask App Factory
def create_app(config_class=Config):
    # Create Flask App
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    limiter.init_app(app)  # Attach the limiter globally

    # Register blueprints
    app.register_blueprint(employee_bp, url_prefix='/employees')
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(order_bp, url_prefix='/orders')
    app.register_blueprint(customer_bp, url_prefix='/customers')
    app.register_blueprint(production_bp, url_prefix='/production')

    return app

# Run the app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

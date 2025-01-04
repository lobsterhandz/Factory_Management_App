from flask_sqlalchemy import SQLAlchemy

# Initialize the database object
db = SQLAlchemy()

# Import models AFTER db initialization to avoid circular imports
from .employee import Employee
from .product import Product
from .order import Order
from .customer import Customer
from .production import Production

from app import create_app  # Import the Flask app factory
from models import db  # Import the initialized db object

# Create the app instance
app = create_app()

# Create tables within the app context
with app.app_context():
    db.create_all()  # Create all database tables
    print("Tables created successfully!")

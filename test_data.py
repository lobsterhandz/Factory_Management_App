from models import db, Employee, Product, Customer, Order, Production
from datetime import datetime

# ---------------------------
# Test Data Setup
# ---------------------------
def seed_test_data():
    try:
        # Clear all existing data
        db.session.query(Order).delete()
        db.session.query(Production).delete()
        db.session.query(Customer).delete()
        db.session.query(Employee).delete()
        db.session.query(Product).delete()

        # Add Employees
        employees = [
            Employee(name='John Doe', position='Manager', email='john.doe@email.com', phone='555-1234'),
            Employee(name='Jane Smith', position='Supervisor', email='jane.smith@email.com', phone='555-5678')
        ]
        db.session.add_all(employees)

        # Add Products
        products = [
            Product(name='Widget A', price=19.99),
            Product(name='Widget B', price=29.99)
        ]
        db.session.add_all(products)

        # Add Customers
        customers = [
            Customer(name='Alice Johnson', email='alice.johnson@email.com', phone='555-4321'),
            Customer(name='Bob Brown', email='bob.brown@email.com', phone='555-8765')
        ]
        db.session.add_all(customers)

        # Add Orders
        orders = [
            Order(customer_id=1, product_id=1, quantity=5, total_price=5 * 19.99),
            Order(customer_id=2, product_id=2, quantity=3, total_price=3 * 29.99)
        ]
        db.session.add_all(orders)

        # Add Production Records
        production = [
            Production(product_id=1, quantity_produced=50, date_produced=datetime(2025, 1, 6)),
            Production(product_id=2, quantity_produced=30, date_produced=datetime(2025, 1, 6))
        ]
        db.session.add_all(production)

        # Commit all data
        db.session.commit()
        print("Test data seeded successfully!")

    except Exception as e:
        db.session.rollback()
        print(f"Error seeding data: {e}")


if __name__ == '__main__':
    from app import create_app
    app = create_app()

    with app.app_context():
        seed_test_data()

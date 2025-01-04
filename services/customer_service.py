from models import db, Customer


class CustomerService:
    @staticmethod
    def create_customer(name, email, phone):
        try:
            if not name or not email or not phone:
                raise ValueError("All fields are required.")

            # Check if email or phone already exists
            existing_customer = Customer.query.filter(
                (Customer.email == email) | (Customer.phone == phone)
            ).first()
            if existing_customer:
                raise ValueError("Customer with this email or phone already exists.")

            # Create a new customer
            new_customer = Customer(
                name=name,
                email=email,
                phone=phone
            )
            db.session.add(new_customer)
            db.session.commit()
            return new_customer
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error creating customer: {str(e)}")

    @staticmethod
    def get_all_customers():
        try:
            return Customer.query.all()
        except Exception as e:
            raise ValueError(f"Error retrieving customers: {str(e)}")

    @staticmethod
    def get_customer_by_id(customer_id):
        try:
            customer = Customer.query.get(customer_id)
            if not customer:
                raise ValueError("Customer not found.")
            return customer
        except Exception as e:
            raise ValueError(f"Error retrieving customer: {str(e)}")

    @staticmethod
    def update_customer(customer_id, name=None, email=None, phone=None):
        try:
            customer = Customer.query.get(customer_id)
            if not customer:
                raise ValueError("Customer not found.")

            # Update fields if provided
            if name:
                customer.name = name
            if email:
                customer.email = email
            if phone:
                customer.phone = phone

            db.session.commit()
            return customer
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error updating customer: {str(e)}")

    @staticmethod
    def delete_customer(customer_id):
        try:
            customer = Customer.query.get(customer_id)
            if not customer:
                raise ValueError("Customer not found.")
            db.session.delete(customer)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error deleting customer: {str(e)}")

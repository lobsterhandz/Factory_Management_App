from models import db, Production, Product
from datetime import datetime


class ProductionService:
    @staticmethod
    def create_production(product_id, quantity_produced, date_produced):
        try:
            # Validate product
            product = Product.query.get(product_id)
            if not product:
                raise ValueError("Product not found.")

            # Validate quantity
            if quantity_produced <= 0:
                raise ValueError("Quantity produced must be greater than zero.")

            # Validate date
            if not isinstance(date_produced, datetime):
                raise ValueError("Invalid date format. Use YYYY-MM-DD.")

            # Create production record
            new_production = Production(
                product_id=product_id,
                quantity_produced=quantity_produced,
                date_produced=date_produced
            )
            db.session.add(new_production)
            db.session.commit()
            return new_production
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error creating production record: {str(e)}")

    @staticmethod
    def get_all_productions():
        try:
            return Production.query.all()
        except Exception as e:
            raise ValueError(f"Error retrieving production records: {str(e)}")

    @staticmethod
    def get_production_by_id(production_id):
        try:
            production = Production.query.get(production_id)
            if not production:
                raise ValueError("Production record not found.")
            return production
        except Exception as e:
            raise ValueError(f"Error retrieving production record: {str(e)}")

    @staticmethod
    def update_production(production_id, quantity_produced=None, date_produced=None):
        try:
            production = Production.query.get(production_id)
            if not production:
                raise ValueError("Production record not found.")

            # Update fields if provided
            if quantity_produced is not None and quantity_produced > 0:
                production.quantity_produced = quantity_produced
            if date_produced is not None and isinstance(date_produced, datetime):
                production.date_produced = date_produced

            db.session.commit()
            return production
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error updating production record: {str(e)}")

    @staticmethod
    def delete_production(production_id):
        try:
            production = Production.query.get(production_id)
            if not production:
                raise ValueError("Production record not found.")
            db.session.delete(production)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error deleting production record: {str(e)}")

from models import db, Product


class ProductService:
    @staticmethod
    def create_product(name, price):
        try:
            if not name or price is None or price < 0:
                raise ValueError("Invalid product data. Name and price are required.")

            new_product = Product(
                name=name,
                price=price
            )
            db.session.add(new_product)
            db.session.commit()
            return new_product
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error creating product: {str(e)}")

    @staticmethod
    def get_all_products():
        try:
            return Product.query.all()
        except Exception as e:
            raise ValueError(f"Error retrieving products: {str(e)}")

    @staticmethod
    def get_product_by_id(product_id):
        try:
            product = Product.query.get(product_id)
            if not product:
                raise ValueError("Product not found.")
            return product
        except Exception as e:
            raise ValueError(f"Error retrieving product: {str(e)}")

    @staticmethod
    def update_product(product_id, name=None, price=None):
        try:
            product = Product.query.get(product_id)
            if not product:
                raise ValueError("Product not found.")

            # Update fields if provided
            if name:
                product.name = name
            if price is not None and price >= 0:
                product.price = price

            db.session.commit()
            return product
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error updating product: {str(e)}")

    @staticmethod
    def delete_product(product_id):
        try:
            product = Product.query.get(product_id)
            if not product:
                raise ValueError("Product not found.")
            db.session.delete(product)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error deleting product: {str(e)}")

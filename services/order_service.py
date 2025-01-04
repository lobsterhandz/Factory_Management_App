from models import db, Order, Product, Customer


class OrderService:
    @staticmethod
    def create_order(customer_id, product_id, quantity):
        try:
            # Validate customer
            customer = Customer.query.get(customer_id)
            if not customer:
                raise ValueError("Customer not found.")

            # Validate product
            product = Product.query.get(product_id)
            if not product:
                raise ValueError("Product not found.")

            # Calculate total price
            total_price = product.price * quantity

            # Create and save order
            new_order = Order(
                customer_id=customer_id,
                product_id=product_id,
                quantity=quantity,
                total_price=total_price
            )
            db.session.add(new_order)
            db.session.commit()

            return new_order
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error creating order: {str(e)}")

    @staticmethod
    def get_all_orders():
        try:
            orders = Order.query.all()
            return orders
        except Exception as e:
            raise ValueError(f"Error retrieving orders: {str(e)}")

    @staticmethod
    def get_order_by_id(order_id):
        try:
            order = Order.query.get(order_id)
            if not order:
                raise ValueError("Order not found.")
            return order
        except Exception as e:
            raise ValueError(f"Error retrieving order: {str(e)}")

    @staticmethod
    def delete_order(order_id):
        try:
            order = Order.query.get(order_id)
            if not order:
                raise ValueError("Order not found.")
            db.session.delete(order)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error deleting order: {str(e)}")

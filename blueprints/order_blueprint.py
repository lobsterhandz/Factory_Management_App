from flask import Blueprint, request, jsonify
from services.order_service import OrderService
from schemas.order_schema import order_schema, orders_schema
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from limiter import limiter 
# Create Blueprint
order_bp = Blueprint('orders', __name__)

# Create an order
@order_bp.route('', methods=['POST'])
@limiter.limit("5 per minute")  # Custom rate limiting
def create_order():
    try:
        data = request.get_json()
        validated_data = order_schema.load(data)
        order = OrderService.create_order(
            customer_id=validated_data['customer_id'],
            product_id=validated_data['product_id'],
            quantity=validated_data['quantity']
        )
        return jsonify(order_schema.dump(order)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Get all orders
@order_bp.route('', methods=['GET'])
@limiter.limit("10 per minute")
def get_orders():
    try:
        orders = OrderService.get_all_orders()
        return jsonify(orders_schema.dump(orders)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Get order by ID
@order_bp.route('/<int:order_id>', methods=['GET'])
@limiter.limit("10 per minute")
def get_order(order_id):
    try:
        order = OrderService.get_order_by_id(order_id)
        return jsonify(order_schema.dump(order)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


# Update order
@order_bp.route('/<int:order_id>', methods=['PUT'])
@limiter.limit("5 per minute")
def update_order(order_id):
    try:
        data = request.get_json()
        validated_data = order_schema.load(data, partial=True)
        order = OrderService.update_order(
            order_id,
            quantity=validated_data.get('quantity')
        )
        return jsonify(order_schema.dump(order)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Delete order
@order_bp.route('/<int:order_id>', methods=['DELETE'])
@limiter.limit("5 per minute")
def delete_order(order_id):
    try:
        OrderService.delete_order(order_id)
        return jsonify({"message": "Order deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

from flask import Blueprint, request, jsonify
from services.customer_service import CustomerService
from schemas.customer_schema import customer_schema, customers_schema
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from limiter import limiter 
# Create Blueprint
customer_bp = Blueprint('customers', __name__)

# Create a customer
@customer_bp.route('', methods=['POST'])
@limiter.limit("5 per minute")  # Custom rate limiting
def create_customer():
    try:
        data = request.get_json()
        validated_data = customer_schema.load(data)
        customer = CustomerService.create_customer(
            name=validated_data['name'],
            email=validated_data['email'],
            phone=validated_data['phone']
        )
        return jsonify(customer_schema.dump(customer)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Get all customers
@customer_bp.route('', methods=['GET'])
@limiter.limit("10 per minute")
def get_customers():
    try:
        customers = CustomerService.get_all_customers()
        return jsonify(customers_schema.dump(customers)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Get customer by ID
@customer_bp.route('/<int:customer_id>', methods=['GET'])
@limiter.limit("10 per minute")
def get_customer(customer_id):
    try:
        customer = CustomerService.get_customer_by_id(customer_id)
        return jsonify(customer_schema.dump(customer)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


# Update customer
@customer_bp.route('/<int:customer_id>', methods=['PUT'])
@limiter.limit("5 per minute")
def update_customer(customer_id):
    try:
        data = request.get_json()
        validated_data = customer_schema.load(data, partial=True)
        customer = CustomerService.update_customer(
            customer_id,
            name=validated_data.get('name'),
            email=validated_data.get('email'),
            phone=validated_data.get('phone')
        )
        return jsonify(customer_schema.dump(customer)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Delete customer
@customer_bp.route('/<int:customer_id>', methods=['DELETE'])
@limiter.limit("5 per minute")
def delete_customer(customer_id):
    try:
        CustomerService.delete_customer(customer_id)
        return jsonify({"message": "Customer deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

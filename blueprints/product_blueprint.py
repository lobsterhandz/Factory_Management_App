from flask import Blueprint, request, jsonify
from services.product_service import ProductService
from schemas.product_schema import product_schema, products_schema
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from limiter import limiter  
# Create Blueprint
product_bp = Blueprint('products', __name__)

# Create a product
@product_bp.route('', methods=['POST'])
@limiter.limit("5 per minute")  # Custom rate limiting
def create_product():
    try:
        data = request.get_json()
        validated_data = product_schema.load(data)
        product = ProductService.create_product(
            name=validated_data['name'],
            price=validated_data['price']
        )
        return jsonify(product_schema.dump(product)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Get all products
@product_bp.route('', methods=['GET'])
@limiter.limit("10 per minute")
def get_products():
    try:
        products = ProductService.get_all_products()
        return jsonify(products_schema.dump(products)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Get product by ID
@product_bp.route('/<int:product_id>', methods=['GET'])
@limiter.limit("10 per minute")
def get_product(product_id):
    try:
        product = ProductService.get_product_by_id(product_id)
        return jsonify(product_schema.dump(product)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


# Update product
@product_bp.route('/<int:product_id>', methods=['PUT'])
@limiter.limit("5 per minute")
def update_product(product_id):
    try:
        data = request.get_json()
        validated_data = product_schema.load(data, partial=True)
        product = ProductService.update_product(
            product_id,
            name=validated_data.get('name'),
            price=validated_data.get('price')
        )
        return jsonify(product_schema.dump(product)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Delete product
@product_bp.route('/<int:product_id>', methods=['DELETE'])
@limiter.limit("5 per minute")
def delete_product(product_id):
    try:
        ProductService.delete_product(product_id)
        return jsonify({"message": "Product deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404
from flask import Blueprint, request, jsonify
from services.product_service import ProductService
from schemas.product_schema import product_schema, products_schema
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Create Blueprint
product_bp = Blueprint('products', __name__)

# Initialize Limiter
limiter = Limiter(
    key_func=get_remote_address,  # Explicitly set key_func
    default_limits=["10 per minute"]
)

# Create a product
@product_bp.route('', methods=['POST'])
@limiter.limit("5 per minute")  # Custom rate limiting
def create_product():
    try:
        data = request.get_json()
        validated_data = product_schema.load(data)
        product = ProductService.create_product(
            name=validated_data['name'],
            price=validated_data['price']
        )
        return jsonify(product_schema.dump(product)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Get all products
@product_bp.route('', methods=['GET'])
@limiter.limit("10 per minute")
def get_products():
    try:
        products = ProductService.get_all_products()
        return jsonify(products_schema.dump(products)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Get product by ID
@product_bp.route('/<int:product_id>', methods=['GET'])
@limiter.limit("10 per minute")
def get_product(product_id):
    try:
        product = ProductService.get_product_by_id(product_id)
        return jsonify(product_schema.dump(product)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


# Update product
@product_bp.route('/<int:product_id>', methods=['PUT'])
@limiter.limit("5 per minute")
def update_product(product_id):
    try:
        data = request.get_json()
        validated_data = product_schema.load(data, partial=True)
        product = ProductService.update_product(
            product_id,
            name=validated_data.get('name'),
            price=validated_data.get('price')
        )
        return jsonify(product_schema.dump(product)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Delete product
@product_bp.route('/<int:product_id>', methods=['DELETE'])
@limiter.limit("5 per minute")
def delete_product(product_id):
    try:
        ProductService.delete_product(product_id)
        return jsonify({"message": "Product deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

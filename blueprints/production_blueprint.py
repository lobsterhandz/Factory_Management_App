from flask import Blueprint, request, jsonify
from services.production_service import ProductionService
from schemas.production_schema import production_schema, productions_schema
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from limiter import limiter  # Import the global limiter from app.py
# Create Blueprint
production_bp = Blueprint('production', __name__)

# Create a production record
@production_bp.route('', methods=['POST'])
@limiter.limit("5 per minute")
def create_production():
    try:
        data = request.get_json()
        validated_data = production_schema.load(data)
        production = ProductionService.create_production(
            product_id=validated_data['product_id'],
            quantity_produced=validated_data['quantity_produced'],
            date_produced=validated_data['date_produced']
        )
        return jsonify(production_schema.dump(production)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Get all production records
@production_bp.route('', methods=['GET'])
@limiter.limit("10 per minute")
def get_productions():
    try:
        productions = ProductionService.get_all_productions()
        return jsonify(productions_schema.dump(productions)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Get production record by ID
@production_bp.route('/<int:production_id>', methods=['GET'])
@limiter.limit("10 per minute")
def get_production(production_id):
    try:
        production = ProductionService.get_production_by_id(production_id)
        return jsonify(production_schema.dump(production)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


# Update production record
@production_bp.route('/<int:production_id>', methods=['PUT'])
@limiter.limit("5 per minute")
def update_production(production_id):
    try:
        data = request.get_json()
        validated_data = production_schema.load(data, partial=True)
        production = ProductionService.update_production(
            production_id,
            quantity_produced=validated_data.get('quantity_produced'),
            date_produced=validated_data.get('date_produced')
        )
        return jsonify(production_schema.dump(production)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Delete production record
@production_bp.route('/<int:production_id>', methods=['DELETE'])
@limiter.limit("5 per minute")
def delete_production(production_id):
    try:
        ProductionService.delete_production(production_id)
        return jsonify({"message": "Production record deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

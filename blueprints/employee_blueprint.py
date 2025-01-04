from flask import Blueprint, request, jsonify
from services.employee_service import EmployeeService
from schemas.employee_schema import employee_schema, employees_schema
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from limiter import limiter 
# Create Blueprint
employee_bp = Blueprint('employees', __name__)

# Create an employee
@employee_bp.route('', methods=['POST'])
@limiter.limit("5 per minute")  # Custom rate limiting
def create_employee():
    try:
        data = request.get_json()
        validated_data = employee_schema.load(data)
        employee = EmployeeService.create_employee(
            name=validated_data['name'],
            position=validated_data['position'],
            email=validated_data['email'],
            phone=validated_data['phone']
        )
        return jsonify(employee_schema.dump(employee)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Get all employees
@employee_bp.route('', methods=['GET'])
@limiter.limit("10 per minute")
def get_employees():
    try:
        employees = EmployeeService.get_all_employees()
        return jsonify(employees_schema.dump(employees)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Get employee by ID
@employee_bp.route('/<int:employee_id>', methods=['GET'])
@limiter.limit("10 per minute")
def get_employee(employee_id):
    try:
        employee = EmployeeService.get_employee_by_id(employee_id)
        return jsonify(employee_schema.dump(employee)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


# Update employee
@employee_bp.route('/<int:employee_id>', methods=['PUT'])
@limiter.limit("5 per minute")
def update_employee(employee_id):
    try:
        data = request.get_json()
        validated_data = employee_schema.load(data, partial=True)
        employee = EmployeeService.update_employee(
            employee_id,
            name=validated_data.get('name'),
            position=validated_data.get('position'),
            email=validated_data.get('email'),
            phone=validated_data.get('phone')
        )
        return jsonify(employee_schema.dump(employee)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Delete employee
@employee_bp.route('/<int:employee_id>', methods=['DELETE'])
@limiter.limit("5 per minute")
def delete_employee(employee_id):
    try:
        EmployeeService.delete_employee(employee_id)
        return jsonify({"message": "Employee deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404
from flask import Blueprint, request, jsonify
from services.employee_service import EmployeeService
from schemas.employee_schema import employee_schema, employees_schema
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Create Blueprint
employee_bp = Blueprint('employees', __name__)

# Initialize Limiter
limiter = Limiter(
    key_func=get_remote_address,  # Explicitly set key_func
    default_limits=["10 per minute"]
)

# Create an employee
@employee_bp.route('', methods=['POST'])
@limiter.limit("5 per minute")  # Custom rate limiting
def create_employee():
    try:
        data = request.get_json()
        validated_data = employee_schema.load(data)
        employee = EmployeeService.create_employee(
            name=validated_data['name'],
            position=validated_data['position'],
            email=validated_data['email'],
            phone=validated_data['phone']
        )
        return jsonify(employee_schema.dump(employee)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Get all employees
@employee_bp.route('', methods=['GET'])
@limiter.limit("10 per minute")
def get_employees():
    try:
        employees = EmployeeService.get_all_employees()
        return jsonify(employees_schema.dump(employees)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Get employee by ID
@employee_bp.route('/<int:employee_id>', methods=['GET'])
@limiter.limit("10 per minute")
def get_employee(employee_id):
    try:
        employee = EmployeeService.get_employee_by_id(employee_id)
        return jsonify(employee_schema.dump(employee)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


# Update employee
@employee_bp.route('/<int:employee_id>', methods=['PUT'])
@limiter.limit("5 per minute")
def update_employee(employee_id):
    try:
        data = request.get_json()
        validated_data = employee_schema.load(data, partial=True)
        employee = EmployeeService.update_employee(
            employee_id,
            name=validated_data.get('name'),
            position=validated_data.get('position'),
            email=validated_data.get('email'),
            phone=validated_data.get('phone')
        )
        return jsonify(employee_schema.dump(employee)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Delete employee
@employee_bp.route('/<int:employee_id>', methods=['DELETE'])
@limiter.limit("5 per minute")
def delete_employee(employee_id):
    try:
        EmployeeService.delete_employee(employee_id)
        return jsonify({"message": "Employee deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

from models import db, Employee


class EmployeeService:
    @staticmethod
    def create_employee(name, position, email, phone):
        try:
            if not name or not position or not email or not phone:
                raise ValueError("All fields are required.")

            new_employee = Employee(
                name=name,
                position=position,
                email=email,
                phone=phone
            )
            db.session.add(new_employee)
            db.session.commit()
            return new_employee
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error creating employee: {str(e)}")

    @staticmethod
    def get_all_employees():
        try:
            return Employee.query.all()
        except Exception as e:
            raise ValueError(f"Error retrieving employees: {str(e)}")

    @staticmethod
    def get_employee_by_id(employee_id):
        try:
            employee = Employee.query.get(employee_id)
            if not employee:
                raise ValueError("Employee not found.")
            return employee
        except Exception as e:
            raise ValueError(f"Error retrieving employee: {str(e)}")

    @staticmethod
    def update_employee(employee_id, name=None, position=None, email=None, phone=None):
        try:
            employee = Employee.query.get(employee_id)
            if not employee:
                raise ValueError("Employee not found.")

            # Update fields if provided
            if name:
                employee.name = name
            if position:
                employee.position = position
            if email:
                employee.email = email
            if phone:
                employee.phone = phone

            db.session.commit()
            return employee
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error updating employee: {str(e)}")

    @staticmethod
    def delete_employee(employee_id):
        try:
            employee = Employee.query.get(employee_id)
            if not employee:
                raise ValueError("Employee not found.")
            db.session.delete(employee)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error deleting employee: {str(e)}")

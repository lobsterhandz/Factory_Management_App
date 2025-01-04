from marshmallow import Schema, fields, validate


class EmployeeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    position = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True, validate=validate.Length(max=100))
    phone = fields.Str(
        required=True,
        validate=[
            validate.Length(min=10, max=20),
            validate.Regexp(r'^\+?1?\d{9,15}$', error="Invalid phone number format.")
        ]
    )
    created_at = fields.DateTime(dump_only=True)


# Example usage
employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

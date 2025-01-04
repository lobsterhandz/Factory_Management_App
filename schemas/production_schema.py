from marshmallow import Schema, fields, validate


class ProductionSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    quantity_produced = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="Quantity must be at least 1.")
    )
    date_produced = fields.Date(
        required=True,
        error_messages={"invalid": "Invalid date format. Use YYYY-MM-DD."}
    )
    created_at = fields.DateTime(dump_only=True)


# Example usage
production_schema = ProductionSchema()
productions_schema = ProductionSchema(many=True)
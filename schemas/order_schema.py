from marshmallow import Schema, fields, validate


class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="Quantity must be at least 1.")
    )
    total_price = fields.Float(dump_only=True)
    created_at = fields.DateTime(dump_only=True)


# Example usage
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

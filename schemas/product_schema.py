from marshmallow import Schema, fields, validate


class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=100)
    )
    price = fields.Float(
        required=True,
        validate=validate.Range(min=0, error="Price must be a positive number.")
    )
    created_at = fields.DateTime(dump_only=True)


# Example usage
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

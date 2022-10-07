from marshmallow import Schema, fields
from marshmallow.validate import Range, OneOf

class ProductSchema(Schema):
    id = fields.Int(autoincrement=True)
    name = fields.Str(required=True)
    description = fields.Str(validate=Range(min=20, max=300))
    price = fields.Int(required=True, validate=Range(min=1, max=99999))
    currency = fields.Str(required=True, validate=OneOf(['₹','$', '€']))
    stock = fields.Int(required=True, validate=Range(min=1,max=999))
    active = fields.Boolean(required=True)



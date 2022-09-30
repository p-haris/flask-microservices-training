from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app import app, restful_api, db, flask_bcrypt
from app.exceptions import ProductNotFountException, InvalidProductPayload, ProductExistsException
from ..models.product import Product
from ..schemas.product_schema import ProductSchema

product_schema = ProductSchema()

#class to create, get and delete products.
class ProductsApi(Resource):
    #Get Products
    def get(self):
        return [product.to_json() for product in Product.query.all()]
        #product is an sqlalchemy object, so converting it into json.

    #create products.
    def  post(self):
        #check for errors at request level
        errors = product_schema.validate(request.json)
        if errors:
            raise InvalidProductPayload(errors, 400)
        existing_product = Product.query.filter_by(name=request.json.get('name')).first()
        if (existing_product is not None):
            raise ProductExistsException(f"Product [{existing_product.name}] already exists!")
        new_product = Product.from_json(request.json)
        db.session.add(new_product)
        db.session.commit()
        return new_product.to_json(), 201

    #delete all products
    def delete(self):
        return [db.session.delete(products) for products in Product.query.all()]

restful_api.add_resource(ProductsApi, '/api/products')
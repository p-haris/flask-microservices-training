from app import db
import enum 
from sqlalchemy import CheckConstraint
# to choose oneof for field currency
################################To create a Product(attributes) Model 

# class currency(enum.Enum):
#     rupees = 'rupees'
#     dollars = 'dollars'
#     euros = 'euros'

# class Product(db.Model):
#     __tablename__ = 'PMS_PRODUCT'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(99))
#     description = db.Column(db.String(255), nullable=True)
#     price = db.Column(db.Integer, db.CheckConstraint('price >= 1 AND price <= 99999'))
#     currency = db.Column(db.Enum(currency))
#     stock = db.Column(db.Integer, db.CheckConstraint('stock >= 1 AND stock <= 999'))
#     active = db.Column(db.Boolean)

    #better not to use checkconstraints here in db table, if it fails, throws an exception to user like sqlerror , which is not a good thing. 
    #So, better give the validation in schema.


class Product(db.Model):
    __tablename__ = 'PMS_PRODUCT'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(99))
    description = db.Column(db.String(255))
    price = db.Column(db.Integer)
    currency = db.Column(db.String(1))
    stock = db.Column(db.Integer)
    active = db.Column(db.Boolean)

    def __init__(self, id, name, description, price, currency, stock, active):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.currency = currency
        self.stock = stock
        self.active = active

    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'price':self.price,
            'currency':self.currency,
            'stock':self.stock,
            'active':self.active
        }

    @staticmethod
    def from_json(json_dct):
        return Product(
            json_dct.get('id'),
            json_dct['name'],
            json_dct['description'],
            json_dct['price'],
            json_dct['currency'],
            json_dct['stock'],
            json_dct['active']
        )
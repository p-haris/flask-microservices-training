#To create a Product(attributes) Model 

from app import db
from marshmallow_enum import Enum
# to choose oneof for field currency

class currency(Enum):
    rupees = 'rupees'
    dollars = 'dollars'
    euros = 'euros'

class Product(db.Model):
    __tablename__ = 'PMS_PRODUCT'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(99))
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Integer)
    currency = db.Column(db.OneOf())

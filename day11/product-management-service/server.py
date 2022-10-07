from app import app, db
from app.api.products import ProductsApi

if __name__ == '__main__':
    db.create_all()
    app.run()
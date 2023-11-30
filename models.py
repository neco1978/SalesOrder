from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def update_user(self, password, role):
      self.password = password
      self.role = role
      db.session.commit()

class Product(db.Model):
    product_code = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    unit_price = db.Column(db.Numeric(10, 2))
    stock_level = db.Column(db.Integer)

    def __init__(self, product_code, name, description, unit_price, stock_level):
        self.product_code = product_code
        self.name = name
        self.description = description
        self.unit_price = unit_price
        self.stock_level = stock_level
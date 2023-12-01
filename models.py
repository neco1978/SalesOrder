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

    def update_product(self, name, description, unit_price, stock_level):
      self.name= name
      self.description= description
      self.unit_price= unit_price
      self.stock_level= stock_level
      db.session.commit()

    def __init__(self, product_code, name, description, unit_price, stock_level):
        self.product_code = product_code
        self.name = name
        self.description = description
        self.unit_price = unit_price
        self.stock_level = stock_level

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.Text)
    phone = db.Column(db.String(15))

    def update_customer(self, name, email, address, phone):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        db.session.commit()

    def __init__(self, name, email, address, phone):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

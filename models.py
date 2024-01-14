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

class Sales_Order(db.Model):
    __tablename__ = 'sales_order'

    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.Date)
    order_number = db.Column(db.String(50), unique=True)
    customer_id = db.Column(db.Integer, db.ForeignKey(Customers.id))
    customer = db.relationship('Customers', backref='orders')
    details = db.relationship('Sales_Order_Details', back_populates='order', cascade='all, delete-orphan')

    def __init__(self, order_date, order_number, customer_id):
        self.order_date = order_date
        self.order_number = order_number
        self.customer_id = customer_id

    def update_order(self, order_date, order_number, customer_id):
        self.order_date = order_date
        self.order_number = order_number
        self.customer_id = customer_id
        db.session.commit()

class Sales_Order_Details(db.Model):
    __tablename__ = 'sales_order_details'

    detail_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(Sales_Order.order_id))
    order = db.relationship('Sales_Order', back_populates='details')
    #product_code = db.Column(db.String(50), db.ForeignKey('product.product_code'))
    product_code = db.Column(db.String(50), db.ForeignKey(Product.product_code))
    product = db.relationship('Product', backref='orderdetails')
    quantity = db.Column(db.Integer)

    def __init__(self, order_id, product_code, quantity):
        self.order_id = order_id
        self.product_code = product_code
        self.quantity = quantity

    def update_order_detail(self, quantity):
        self.quantity = quantity
        db.session.commit()
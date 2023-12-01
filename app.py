from flask import Flask, render_template, request, redirect, url_for, session
from models import Users, db
from models import Product  # Import the Product model

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secret key of your choice
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5430/salesdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    user = Users.query.filter_by(username=username, password=password).first()

    if user:
        session['username'] = username
        session['role'] = user.role
        return redirect(url_for('menu'))
    else:
        return f"Invalid username or password. Please try again.{username},{password},{user}"

@app.route('/menu')
def menu():
    if 'username' in session:
        return render_template('menu.html')
    else:
        return redirect(url_for('login'))

@app.route('/users')
def users():
    # Assuming you have a User model defined in models.py from models import User

    # Fetch all users from the database
    users = Users.query.all()

    return render_template('users.html', users=users)

@app.route('/delete_user/<username>', methods=['DELETE'])
def delete_user(username):
    # Get the currently logged-in username from the session
    current_username = session.get('username')

    if current_username == username:
        return 'You cannot delete your own user account.', 403

    user = Users.query.filter_by(username=username).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return 'User deleted successfully', 200
    else:
        return 'User not found', 404

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

@app.route('/create_user')
def create_user():
    return render_template('create_user.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    role = request.form['role']

    # Create a new user in the database
    new_user = Users(username=username, password=password, role=role)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('users'))
    #return render_template('menu.html')

@app.route('/update_user/<username>', methods=['POST'])
def update_user(username):
    password = request.form['password']
    role = request.form['role']

    user = Users.query.filter_by(username=username).first()
    if user:
        user.update_user(password, role)
        return 'User updated successfully', 200
    else:
        return 'User not found', 404

@app.route('/update_user/<username>')
def update_user_page(username):
    user = Users.query.filter_by(username=username).first()
    if user:
        return render_template('update_user.html', user=user)
    else:
        return 'User not found', 404

# New routes for Products
@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/create_product')
def create_product():
    return render_template('create_product.html')

@app.route('/add_product', methods=['POST'])
def add_product():
    product_code = request.form['productCode']
    name = request.form['name']
    description = request.form['description']
    unit_price = request.form['unitPrice']
    stock_level = request.form['stockLevel']

    new_product = Product(product_code=product_code, name=name, description=description, unit_price=unit_price, stock_level=stock_level)
    db.session.add(new_product)
    db.session.commit()

    return redirect(url_for('products'))

#@app.route('/delete_product/<product_code>', methods=['DELETE'])
#def delete_product(product_code):
#    #product = Product.query.filter_by(product_code=product_code).first()
#    product = session.get('product_code')
#    if product:
#        db.session.delete(product)
#        db.session.commit()
#        return jsonify(message='Product deleted successfully'), 200
#    else:
#        return jsonify(error='Product not found'), 404

####
@app.route('/delete_product/<product_code>', methods=['DELETE'])
def delete_product(product_code):
    product = Product.query.filter_by(product_code=product_code).first()
    if product:
        db.session.delete(product)
        db.session.commit()
        return 'Product deleted successfully', 200
    else:
        return 'Product not found', 404

@app.route('/update_product/<product_code>')
def update_product_page(product_code):
    product = Product.query.filter_by(product_code=product_code).first()
    if product:
        return render_template('update_product.html', product=product)
    else:
        return 'Product not found', 404

@app.route('/update_product', methods=['POST'])
def update_product():
    product_code = request.form['product_code']
    name = request.form['name']
    description = request.form['description']
    unit_price = request.form['unit_price']
    stock_level = request.form['stock_level']

    product = Product.query.filter_by(product_code=product_code).first()
    if product:
        product.name = name
        product.description = description
        product.unit_price = unit_price
        product.stock_level = stock_level
        db.session.commit()
        return redirect(url_for('products.html'))
    else:
        return 'Product not found', 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

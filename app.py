from flask import Flask, render_template, request, redirect, url_for, session
from models import Users, db

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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

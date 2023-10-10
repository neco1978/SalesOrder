# SalesOrder

# Sales Order Management System

## Description
This is a simple Sales Order Management System implemented using Flask and PostgreSQL. It allows users to manage sales orders, products, customers, invoices, and delivery notes.

## Features
- User authentication with role-based access control (ADMIN, MONITORING)
- CRUD operations for users, products, customers, sales orders, invoices, and delivery notes
- Interactive menu with dropdown navigation
- Responsive design for easy use on different devices
- Search and filter functionalities for user list
- Confirmations for critical actions (delete user, logout)

## Installation
1. Clone the repository to your local machine.
2. Create a Python virtual environment.

3. Activate the virtual environment.
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
4. Install the required packages.

5. Set up the PostgreSQL database.
- Create a database named `salesdb`.
- Update the database connection URI in `app.py` to match your PostgreSQL configuration.

6. Run the application.


## Usage
1. Access the application in your web browser at `http://localhost:5000`.
2. Log in with your username and password.
3. Use the menu on the left to navigate between different sections (Inbox, Users, Customers, Products, Orders, Invoices, Delivery Notes).
4. Perform CRUD operations as needed.

## Contributing
Pull requests and bug reports are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT License](LICENSE)


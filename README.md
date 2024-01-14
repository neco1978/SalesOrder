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
- Run data_model.sql under the model directory to create required tables and data structure

6. Run the application.


## Usage
1. Access the application in your web browser at `http://localhost:5000`.
2. Log in with your username and password.
3. Use the menu on the left to navigate between different sections (Inbox, Users, Customers, Products, Orders, Invoices, Delivery Notes).
4. Perform CRUD operations as needed.

## Contributing
Pull requests and bug reports are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Technical Details
The project you've been working on follows a basic web application design pattern using the Flask framework for Python. Here's a breakdown of the design pattern:

1. Model-View-Controller (MVC):

Model: This part handles the data and the database operations. It interacts with the database (using SQLAlchemy in your case) and defines the structure of your data (Users in your case).

View: The view is responsible for rendering the HTML templates that the user interacts with. It's what the user sees and interacts with in their browser. In your project, these are the HTML files stored in the templates folder.

Controller: The controller handles the logic that takes user input and decides what to do with it. In this project, it's the Flask application itself. The routes you've defined in app.py are the controllers. They handle requests from the user, interact with the model (if necessary), and render the appropriate view.

2. Templates: You're using HTML templates for the views. These templates are rendered by Flask and may contain placeholders (like {{ user.username }}) that are replaced with actual data before being sent to the user's browser.

3. Database: You're using PostgreSQL as your database. The Users model (defined in models.py) interacts with this database using SQLAlchemy, which provides an Object-Relational Mapping (ORM) to interact with the database in a more Pythonic way.

4. Static Files: You have a static folder which typically contains files like CSS, JavaScript, and images. These files are not rendered by Flask, but they're served directly by the web server.

5. Styling: You've used CSS for styling your web pages. This controls the look and feel of your application.

6. JavaScript: You've also used JavaScript, particularly for handling AJAX requests and performing dynamic updates to the web page.

7. Session Management: You're using sessions in Flask to keep track of logged-in users.

8. AJAX Requests: You've used JavaScript and jQuery to make asynchronous requests to the server, allowing for dynamic updates without refreshing the whole page.

9. Error Handling: You have some basic error handling in place. For example, when a user tries to delete their own account.

10. User Authentication: Your application handles user authentication by checking the username and password against records in the database.

Overall, your application has a clear separation of concerns between the model, view, and controller. It uses a relational database for data storage, provides a web-based UI for interaction, and incorporates client-side scripting for dynamic behavior. It's a good starting point for a web application, and you can continue to build on it by adding more features and refining the existing ones.

## License
[MIT License](LICENSE)


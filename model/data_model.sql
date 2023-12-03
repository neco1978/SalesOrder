CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    password VARCHAR(120) NOT NULL,
	role VARCHAR(50) CONSTRAINT valid_roles CHECK (role IN ('ADMIN', 'MONITORING','USER')) NOT NULL
);

-- Create Product Table
CREATE TABLE product (
    product_code VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    unit_price DECIMAL(10,2),
    stock_level INTEGER
);

-- Create Customer Table
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE,
    email VARCHAR(120) UNIQUE,
    address TEXT,
    phone VARCHAR(15)
);

-- Create Sales Order Table
CREATE TABLE sales_order (
    order_id SERIAL PRIMARY KEY,
    order_date DATE,
    order_number VARCHAR(50) UNIQUE,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Create Sales Order Details Table
CREATE TABLE sales_order_details (
    detail_id SERIAL PRIMARY KEY,
    order_id INTEGER,
    product_code VARCHAR(50),
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES sales_order(order_id),
    FOREIGN KEY (product_code) REFERENCES product(product_code)
);

-- Create Invoice Table
CREATE TABLE invoice (
    invoice_number VARCHAR(50) PRIMARY KEY,
    order_id INTEGER UNIQUE,
    date DATE,
    total_amount DECIMAL(10,2),
    payment_status VARCHAR(20),
    FOREIGN KEY (order_id) REFERENCES sales_order(order_id)
);

-- Create Delivery Note Table
CREATE TABLE delivery_note (
    delivery_note_number VARCHAR(50) PRIMARY KEY,
    order_id INTEGER UNIQUE,
    date DATE,
    delivery_status VARCHAR(20),
    signature VARCHAR(100),
    FOREIGN KEY (order_id) REFERENCES sales_order(order_id)
);

insert into users(username, password, role) values('nevzat','password','ADMIN');
insert into users(username, password, role) values('mehmet','password','ADMIN');
insert into users(username, password, role) values('jack','password','MONITORING');
insert into users(username, password, role) values('adam','password','USER');

insert into sales_order (order_date, order_number, customer_id)  values(current_date, 'SD00013',2);

insert into sales_order_details (order_id, product_code, quantity) values (2, 100, 8);
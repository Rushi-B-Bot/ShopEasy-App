

-- Switch to PostgreSQL User(Start the pg sql)

-- PostgreSQL creates a default postgres system user.-
1) sudo -i -u postgres 
2) enter the password (ubantu profile)


-- Open PostgreSQL Shell
1) psql

-- Exit with and clear the scree
1) \q
2) cntl + L || \! clear

-- Check the db
1) \l

-- List users/roles:
1) \du

-- Create the DB
1) CREATE DATABASE ecommerce OWNER asusubuntu

-- Show current database
1) SELECT current_database();

-- Connect to database:
1) \c ecommerce


-- Show Tables in Current Database
1) \dt --> check the all table present in that db
2) \dt *.*

-- Show Table Structure
1) \d users --> (Table_name)


--  Note 
1) Every SQL command must end with: [ ; ] 



connnection to the backed: 
const pool = new Pool({
  user: 'asusubuntu',
  host: 'localhost',
  database: 'ecommerce',
  password: 'Rushikesh@99',
  port: 5432
})

3️⃣ Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

4️⃣ Products Table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200),
    description TEXT,
    price NUMERIC(10,2),
    stock INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
5️⃣ Cart Table

Stores products a user wants to buy.

CREATE TABLE cart (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    product_id INT REFERENCES products(id),
    quantity INT DEFAULT 1
);
6️⃣ Orders Table
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    total_price NUMERIC(10,2),
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
7️⃣ Order Items Table

Stores products inside each order.

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id),
    product_id INT REFERENCES products(id),
    quantity INT,
    price NUMERIC(10,2)
);
8️⃣ Table Relationship
users
  │
  └── orders
        │
        └── order_items
                │
                └── products

users
  │
  └── cart
        │
        └── products
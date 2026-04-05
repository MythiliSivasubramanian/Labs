/*
SQL Foundations :

1. Table creation: products, orders & categories
2. Insert values into each tables

Tasks:

*/

-- 1. Table creation: products 
CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category_id INTEGER,    
    price INTEGER
);

-- 1 Table creation : orders
CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER,
    customer_id INTEGER,
    order_date DATE
);

-- 1. Table creation: categories 
CREATE TABLE IF NOT EXISTS categories(
    category_id INTEGER PRIMARY KEY,
    category_name TEXT
);

-- 2. Insert values to Table products
DELETE FROM products;
INSERT INTO products(product_id, product_name, category_id,	price) VALUES
    (1, 'Laptop', 1, 1200),
    (2, 'Smartphone', 1, 800),
    (3, 'Headphones', 2, 150),
    (4, 'Monitor', 3, 300),
    (5, 'Keyboard', 2, 50),
    (6, 'Gaming Mouse', 2, 70),
    (7, 'Desk Lamp', 4, 40),
    (8, 'USB-C Cable', 2, 20),
    (9, 'Chair', 4, 100),
    (10,'Tablet', 1, 600);

-- 2. Insert values to Table orders
DELETE FROM orders;
INSERT INTO orders(order_id, product_id, quantity, customer_id, order_date) VALUES
    (101, 1, 2, 1001, '2026-01-01'),
    (102, 3, 5, 1002, '2026-01-02'),
    (103, 2, 1, 1003, '2026-01-03'),
    (104, 5, 3, 1001, '2026-01-03'),
    (105, 6, 2, 1002, '2026-01-04'),
    (106, 1, 1, 1003, '2026-01-04'),
    (107, 4, 2, 1004, '2026-01-05'),
    (108, 7, 4, 1001, '2026-01-05'),
    (109, 8, 10, 1002, '2026-01-06'),
    (110, 9, 1, 1003, '2026-01-06'),
    (111, 10, 2, 1004, '2026-01-07'),
    (112, 2, 3, 1001, '2026-01-07');


-- 3. Insert into categories table
DELETE FROM categories;
INSERT INTO categories(category_id, category_name) VALUES  
    (1, 'Electronics'),
    (2, 'Accessories'),   
    (3, 'Displays'),  
    (4, 'Furniture');

-- 4. Show all products with their product name and price, sorted by price descending
SELECT product_name, price
FROM products
ORDER BY price DESC;

DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    prod_description VARCHAR (255),
    quantity INT,
    purchase_price INT,
    selling_price INT,
    supplier_id INT REFERENCES suppliers(id)
);
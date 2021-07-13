from db.run_sql import run_sql

from models.supplier import Supplier
from models.product import Product

import repositories.supplier_repository as supplier_repository

def save(product):
    sql = "INSERT INTO products (product_name, prod_description, quantity, purchase_price, selling_price, supplier_id) VALUES (%s, %s, %s, %s, %s. %s) RETURNING *"
    values = [product.product_name, product.prod_description, product.quantity, product.purchase_price, product.selling_price, product.supplier.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        supplier = supplier_repository.select(row['supplier_id'])
        product = Product(row['product_name'], row['prod_description'], row['quantity'], row['quantity'], row['purchase_price'], row['selling_price'], supplier, row['id'])
        products.append(product)
    return products

def select(id):
    pass

def delete_all():
    pass

def delete(id):
    pass

def update(product):
    pass
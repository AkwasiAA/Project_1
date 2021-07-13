from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier

def save(supplier):
    sql = "INSERT INTO suppliers (supplier_name) VALUES (%s) RETURNING *"
    values = [supplier.supplier_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    supplier.id = id
    return supplier

def select_all():
    suppliers = []

    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)

    for row in results:
        supplier = Supplier(row['supplier_name'], row['id'])
        suppliers.append(supplier)
    return suppliers

def select(id):
    supplier = None
    sql = "SELECT * FROM suppliers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        supplier = Supplier(result['supplier_name'], result['id'])
    return supplier

def delete_all():
    sql = "DELETE  FROM suppliers"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM suppliers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(supplier):
    sql = "UPDATE suppliers SET (supplier_name) = (%s) WHERE id = %s"
    values = [supplier.supplier_name, supplier.id]
    run_sql(sql, values)

def products(supplier):
    products = []

    sql = "SELECT * FROM products WHERE supplier_id = %s"
    values = [supplier.id]
    results = run_sql(sql, values)

    for row in results:
        product = Product(row['product_name'], row['prod_description'], row['quantity'], row['purchase_price'], row['selling_price'], supplier, row['id'] )
        products.append(product)
    return products
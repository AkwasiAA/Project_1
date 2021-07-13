from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

products_blueprint = Blueprint("products", __name__)


# INDEX
# GET '/products'
@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", all_products = products)

# NEW
# GET '/products/new'
@products_blueprint.route("/products/new", methods=['GET'])
def new_product():
    suppliers = supplier_repository.select_all()
    return render_template("products/new.html", all_suppliers = suppliers)


# CREATE
# POST '/products'
@products_blueprint.route("/products", methods =['POST'])
def create_product():
    product_name = request.form['product_name']
    prod_description = request.form['prod_description']
    quantity = request.form['quantity']
    purchase_price = request.form['purchase_price']
    selling_price = request.form['selling_price']
    supplier = supplier_repository.select(request.form['supplier_id'])
    product = Product(product_name, prod_description, quantity, purchase_price, selling_price, supplier)
    product_repository.save(product)
    return redirect('/products')

# SHOW
# GET '/products/<id>'

# EDIT
# GET '/products/<id>/edit'

# UPDATE
# PUT/POST '/products/<id>'

# DELETE
# DELETE '/products/<id>'
@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')
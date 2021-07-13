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


# CREATE
# POST '/products'

# SHOW
# GET '/products/<id>'

# EDIT
# GET '/products/<id>/edit'

# UPDATE
# PUT/POST '/products/<id>'

# DELETE
# DELETE '/products/<id>'
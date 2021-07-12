from flask import Flask
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

products_blueprint = Blueprint("products", __name__)






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
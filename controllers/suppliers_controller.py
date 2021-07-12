from flask import Flask
from flask import Blueprint
from models.supplier import Supplier
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

suppliers_blueprint = Blueprint("suppliers", __name__)






# NEW
# GET '/suppliers/new'

# CREATE
# POST '/suppliers'

# SHOW
# GET '/suppliers/<id>'

# EDIT
# GET '/suppliers/<id>/edit'

# UPDATE
# PUT/POST '/suppliers/<id>'

# DELETE
# DELETE '/suppliers/<id>'
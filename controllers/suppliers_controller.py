from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.supplier import Supplier
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

suppliers_blueprint = Blueprint("suppliers", __name__)

# INDEX
# GET '/products'
@suppliers_blueprint.route("/suppliers")
def products():
    suppliers = supplier_repository.select_all()
    return render_template("suppliers/index.html", all_suppliers = suppliers)


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
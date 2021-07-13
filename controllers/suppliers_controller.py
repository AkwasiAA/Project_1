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
@suppliers_blueprint.route("/suppliers/new", methods=['GET'])
def new_supplier():
    products = product_repository.select_all()
    return render_template("suppliers/new.html", all_products = products)

# CREATE
# POST '/suppliers'
@suppliers_blueprint

# SHOW
# GET '/suppliers/<id>'

# EDIT
# GET '/suppliers/<id>/edit'

# UPDATE
# PUT/POST '/suppliers/<id>'

# DELETE
# DELETE '/suppliers/<id>'
@suppliers_blueprint.route("/suppliers/<id>/delete", methods=['POST'])
def delete_supplier(id):
    supplier_repository.delete(id)
    return redirect("/suppliers")

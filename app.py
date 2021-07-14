from repositories import product_repository, supplier_repository
from flask import Flask, render_template

from controllers.products_controller import products_blueprint
from controllers.suppliers_controller import suppliers_blueprint
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

app = Flask(__name__)

app.register_blueprint(products_blueprint)

@app.route('/')
def home():
    return render_template('index.html')


app.register_blueprint(suppliers_blueprint)

app.route('suppliers/index')
def suppliers():
    suppliers = supplier_repository.select_all()
    return render_template('suppliers/index.html', all_suppliers = suppliers)

if __name__ == '__main__':
    app.run(debug=True)
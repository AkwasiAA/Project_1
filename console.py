import pdb
from models.product import Product
from models.supplier import Supplier

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

# product_repository.delete_all()
# supplier_repository.delete_all()

supplier1 = Supplier("Rado Wholesale PLC")
supplier_repository.save(supplier1)
supplier2 = Supplier("Montredo Watches Ltd")
supplier_repository.save(supplier2)
supplier3 = Supplier("Baume & Mercier SA")
supplier_repository.save(supplier3)

product1 = Product("Rado Coupole Classic", "R228: Black Leather 37mm", 2, 750, 1159, supplier1)
product_repository.save(product1)

product2 = Product("Junghans Meister Classic", "027/3000: Green 38mm Limited Edition", 1, 1050, 1500, supplier2)
product_repository.save(product2)

product3 = Product("Baume & Mercier Classima", "MOA1: Brown Leather 40mm", 4, 1000, 1795, supplier3)
product_repository.save(product3)
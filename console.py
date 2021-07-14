import pdb
from models.product import Product
from models.supplier import Supplier

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

product_repository.delete_all()
supplier_repository.delete_all()

supplier1 = Supplier("Rado Wholesale PLC")
supplier_repository.save(supplier1)
supplier2 = Supplier("Montredo Watches Ltd")
supplier_repository.save(supplier2)
supplier3 = Supplier("Baume & Mercier SA")
supplier_repository.save(supplier3)
supplier4 = Supplier("Frederique Constant SA")
supplier_repository.save(supplier4)
supplier5 = Supplier("Junghans Uhren GmbH")
supplier_repository.save(supplier5)

product_1 = Product("Rado Coupole Classic", "R228: Black Leather 37mm", 6, 750, 1159, supplier1)
product_repository.save(product_1)

product_2 = Product("Junghans Meister Classic", "027/3000: Green 38mm Limited Edition", 3, 1050, 1500, supplier5)
product_repository.save(product_2)

product_3 = Product("Baume & Mercier Classima", "MOA1: Brown Leather 40mm", 4, 1000, 1795, supplier3)
product_repository.save(product_3)

product_4 = Product("Audemars Piguet Rare Octagonal", "15062002: Green Enamel 31mm", 1, 7950, 9250, supplier2)
product_repository.save(product_4)

product_5 = Product("Rolex Datejust", "16233: Steel and Yellow Gold 36mm", 4, 6000, 7195, supplier2)
product_repository.save(product_5)
#--main.py je glavna skripta za implementaciju metoda iz 'product.py' i 'product_manager.py'

from product import Product
from product_manager import ProductManager
from Cart import Cart

#--Proizvodi:
product_1 = Product('Fender Stratocaster', 250000, 15)
product_2 = Product('Fender Jazz bass', 310000, 10)
product_3 = Product('Fender Telecaster', 180000, 10)
product_4 = Product('Fender Precision bass', 300000, 5)

#--Promena na lageru:
product_1.update_goods(10)
product_3.update_goods(5)

#--Product Manager:
product_manager = ProductManager()

#--Dodavanje na lager:
#--uklonjeno

#--Informacije:
#--uklonjeno

#--Cart test:
cart = Cart()

cart.add_to_cart(product_2)
cart.add_to_cart(product_4)

cart.get_cart_items()
cart.get_cart_total()


product_1 = Product('Fender Stratocaster', 250000, 15)
product_2 = Product('Fender Jazz bass', 310000, 10)
product_3 = Product('Fender Telecaster', 180000, 10)
product_4 = Product('Fender Precision bass', 300000, 5)



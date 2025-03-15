#--cart.py sadrzi klasu za korpu kupca:

from product import Product

class Cart:
    def __init__(self):
        
        #--Potrosacka korpa:
        self.cart_items = []

    #--Dodavanje u korpu:
    def add_to_cart(self, product):
        if isinstance(product, Product):
            self.cart_items.append(product)
            return f">.✅ - Proizvod '{product.name}' dodat u korpu!"
        else:
            return ">.⚠️ - Greska! Samo proizvodi iz prodavnice mogu biti dodati u korpu."
        
    #--Ukupna vrednost proizvoda u korpi:
    def get_cart_total(self):
        cart_total = sum([product.price * product.quantity for product in self.cart_items])
        print(f">.🛒 - Ukupna cena u korpi: {cart_total}")

    #--Proizvodi u korpi:
    def get_cart_items(self):
        if not self.cart_items:
            print(">.❌ - Vasa korpa je prazna!")
        
        print("-" * 50)
        print(">.🛒 - Vasa korpa: ")
        for item in self.cart_items:
            print(f"{item.get_info()}")
        print("-" * 50)


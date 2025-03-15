#--product_manager.py sadrzi klasu za upravljanje proizvodima:

from product import Product

class ProductManager:
    def __init__(self):

        #--Lista proizvoda:
        self.product_list = []

    #--Dodajemo proizvode na lager:
    def add_product(self, product):
        if isinstance(product, Product):
            self.product_list.append(product)
            print(f">.✅ - Proizvod '{product.name}' dodat na listu!")
        else:
            print(">.⚠️ - Greska! Samo proizvodi iz prodavnice mogu biti na lageru.")
    
    #--Informacije o lageru:
    def get_stock(self):
        if not self.product_list:
            print(">.❌ - Nema proizvoda na lageru.")
        
        print("-" * 50)
        print(">.📃 - Lista proizvoda:")        
        for product in self.product_list:
            print(f"{product.get_info()}")

        print("-" * 50)

    #--Ukupna cena na lageru:
    def get_total_price(self):
        total_price = sum(product.price * product.quantity for product in self.product_list)
        print(f">.💵 - Ukupna cena svih proizvoda: {total_price:.2f}")

    #--Uklanjanje proizvoda:
    def remove_product(self, product):
        if isinstance(product, Product):
            if product in self.product_list:
                self.product_list.remove(product)
                print(f">.📤 - Proizvod '{product}' uspesno uklonjen sa lagera.")
            else:
                print(f">.⚠️ - Greska! Proizvod '{product}' ne postoji na lageru!")
        else:
            print(f">.⚠️ - Greska! Unesite proizvod sa naseg lagera!")


        #--Uklanjanje proizvoda:
    def remove_product(self, product):
        if isinstance(product, Product):
            if product in self.product_list:
                self.product_list.remove(product)
                print(f">.📤 - Proizvod '{product}' uspesno uklonjen sa lagera.")
            else:
                print(f">.⚠️ - Greska! Proizvod '{product}' ne postoji na lageru!")
        else:
            print(f">.⚠️ - Greska! Unesite proizvod sa naseg lagera!")


       #--Ukupna cena na lageru:
    def get_total_price(self):
        total_price = sum(product.price * product.quantity for product in self.product_list)
        print(f">.💵 - Ukupna cena svih proizvoda: {total_price:.2f}")      
                
    

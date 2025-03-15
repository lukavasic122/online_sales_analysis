#--product.py sadrzi klasu za proizvode:
#--Prikaz informacija i azuriranje kolicine proizvoda

class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    #--Prikaz informacija o proizvodu:
    def get_info(self):
        return f">.📦 - Proizvod '{self.name}' | Cena: {self.price} | Kolicina: {self.quantity}"

    #--Azuriranje kolicine proizvoda:
    def update_goods(self, amount):
        if isinstance(amount, int):
            self.quantity += amount
            return f">.⬆️ - Kolicina '{self.name}' azurirana! Kolicina: {self.quantity}"
        else:
            return f">.⚠️ - Greska! Molim Vas, unesite ceo broj (e.g. 10)!"

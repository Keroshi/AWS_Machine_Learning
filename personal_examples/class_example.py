class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.shirt_color = shirt_color
        self.shirt_size = shirt_size
        self.shirt_style = shirt_style
        self.shirt_price = shirt_price

    def change_price(self, new_price):
        self.shirt_price = new_price

    def discount_price(self, discount):
        return self.shirt_price * (1 - discount)


new_shirt = Shirt('blue', 'Small', 10, 5)
print(new_shirt.shirt_color)

shirt_1 = Shirt("Yellow", "Small", "Short Sleeve", 5)
shirt_2 = Shirt("Blue", "Medium", "Long Sleeve", 10)
shirt_3 = Shirt("Red", "Large", "Short Sleeve", 7)

shirt_catalogue = [shirt_1, shirt_2, shirt_3]

for shirt in shirt_catalogue:
    print(shirt.shirt_color)

new_shirt.change_price(17)
print(new_shirt.shirt_price)

new_shirt.discount_price(0.05)

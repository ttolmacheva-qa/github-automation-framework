class ShoppingCart:

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item_name):
        self.items.append(item_name)
        print(f"Товар {item_name} добавлен в корзину")

my_cart = ShoppingCart("Anna")

my_cart.add_item("Laptop")
my_cart.add_item("Mouse")

print(len(my_cart.items))
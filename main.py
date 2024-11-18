class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.price:.2f} грн (Доступно: {self.quantity})"

    def is_available(self, requested_quantity):
        return self.quantity >= requested_quantity


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.is_available(quantity):
            if product.name in self.items:
                self.items[product.name]['quantity'] += quantity
            else:
                self.items[product.name] = {'product': product, 'quantity': quantity}
            product.quantity -= quantity
            print(f"Додано {quantity} шт. {product.name} до кошика.")
        else:
            print(f"Недостатньо товару {product.name} в наявності!")

    def remove_product(self, product_name, quantity):
        if product_name in self.items:
            item = self.items[product_name]
            if item['quantity'] <= quantity:
                quantity_to_return = item['quantity']
                item['product'].quantity += quantity_to_return
                del self.items[product_name]
                print(f"Видалено {quantity_to_return} шт. {product_name} з кошика.")
            else:
                item['quantity'] -= quantity
                item['product'].quantity += quantity
                print(f"Видалено {quantity} шт. {product_name} з кошика.")
        else:
            print(f"Товар {product_name} відсутній у кошику.")

    def calculate_total(self):
        total = sum(item['product'].price * item['quantity'] for item in self.items.values())
        return total

    def show_cart(self):
        if not self.items:
            print("Кошик порожній.")
        else:
            print("Ваш кошик:")
            for item_name, item_details in self.items.items():
                print(f"{item_name}: {item_details['quantity']} шт. - {item_details['product'].price:.2f} грн/шт.")
            print(f"Загальна вартість: {self.calculate_total():.2f} грн")

product1 = Product("Молоко", 30.0, 50)
product2 = Product("Хліб", 20.0, 100)
product3 = Product("Сир", 80.0, 20)

cart = Cart()

cart.add_product(product1, 2)
cart.add_product(product2, 5)
cart.add_product(product3, 1)

cart.show_cart()

cart.remove_product("Хліб", 2)

cart.show_cart()


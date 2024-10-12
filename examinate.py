class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.price}$ за шт. (в наявності: {self.quantity})"


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if quantity <= 0:
            print("Неможливо додати від'ємну або нульову кількість товару.")
            return

        if quantity <= product.quantity:
            if product.name in self.items:
                self.items[product.name]['quantity'] += quantity
            else:
                self.items[product.name] = {'product': product, 'quantity': quantity}

            product.quantity -= quantity
            print(f"Додано {quantity} шт. {product.name} у кошик.")
        else:
            print(f"Недостатньо {product.name} на складі! В наявності: {product.quantity}")

    def remove_product(self, product):
        if product.name in self.items:
            quantity_in_cart = self.items[product.name]['quantity']
            product.quantity += quantity_in_cart
            del self.items[product.name]
            print(f"{product.name} видалено з кошика.")
        else:
            print(f"{product.name} не знайдено в кошику.")

    def clear_cart(self):
        for item in self.items.values():
            item['product'].quantity += item['quantity']
        self.items.clear()
        print("Кошик очищено.")

    def total_price(self):
        total = sum(item['product'].price * item['quantity'] for item in self.items.values())
        return total

    def apply_discount(self, discount_threshold, discount_percentage):
        total = self.total_price()
        if total > discount_threshold:
            discount = total * (discount_percentage / 100)
            total -= discount
            print(f"Застосовано знижку {discount_percentage}%! Загальна вартість після знижки: {total}$.")
        else:
            print(f"Щоб отримати знижку, потрібно витратити більше {discount_threshold}$.")

        return total

    def __str__(self):
        if not self.items:
            return "Кошик порожній."

        cart_content = "Кошик:\n"
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            cart_content += f"{product.name} x{quantity} = {product.price * quantity}$\n"

        return cart_content + f"Загальна вартість: {self.total_price()}$"



def shop_interface(cart, products):
    product_dict = {product.name.lower(): product for product in products}

    while True:
        print("\nДоступні товари:")
        for product in products:
            print(product)

        choice = input("Введіть назву товару для додавання до кошика (або 'q' для виходу): ").lower()

        if choice == 'q':
            break

        if choice in product_dict:
            try:
                quantity = int(input(f"Скільки одиниць {product_dict[choice].name} ви хочете додати? "))
                cart.add_product(product_dict[choice], quantity)
            except ValueError:
                print("Будь ласка, введіть коректну кількість.")
        else:
            print("Товар не знайдено. Спробуйте ще раз.")

    print("\nВаш кошик:")
    print(cart)



apple = Product("Яблуко", 0.5, 100)
banana = Product("Банан", 0.3, 50)
orange = Product("Апельсин", 0.8, 30)
grape = Product("Виноград", 1.2, 20)
watermelon = Product("Кавун", 3.0, 10)
pineapple = Product("Ананас", 2.5, 15)
peach = Product("Персик", 1.0, 40)
kiwi = Product("Ківі", 0.7, 35)
mango = Product("Манго", 1.8, 25)
strawberry = Product("Полуниця", 2.0, 50)
blueberry = Product("Чорниця", 2.5, 40)


cart = ShoppingCart()


products = [apple, banana, orange, grape, watermelon, pineapple, peach, kiwi, mango, strawberry, blueberry]
shop_interface(cart, products)


cart.apply_discount(10, 10)


if input("Бажаєте очистити кошик? (так/ні): ").lower() == "так":
    cart.clear_cart()
    print(cart)

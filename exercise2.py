# Exercise 2 - Turn the shopping cart program into an object-oriented program
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Store:
    def __init__(self, items):
        self.items = items


class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, store):
        item_name = input('To add an item please enter a name ')
        if not any(item.name == item_name for item in store.items):
            print("item not available... returning")

        else:
            item_to_add_from_store = next((item for item in store.items if item.name == item_name), None)
            print(f'The price is {item_to_add_from_store.price}')
            if any(item.name == item_name for item in self.items):
                answer = input(f'''{item_name} is already inside of your cart would you like to add more? 
            y for yes n for no ''')
                if answer == 'y':
                    amount_to_add = input('how many would you like to add? ')
                    item_to_add = next((item for item in self.items if item.name == item_name), None)
                    item_to_add.quantity += int(amount_to_add)

            else:
                quantity_to_add = input("how many would you like? ")
                item_to_add = Item(item_name, item_to_add_from_store.price, int(quantity_to_add))
                self.items.append(item_to_add)
                item_to_add_from_store.quantity -= int(quantity_to_add)

    def checkout(self):
        total = 0.0
        for item in self.items:
            total = total + item.quantity * item.price
        print('''.
    .
    .
    . Thanks for shopping! Here is your receipt: ''', '$', total, 'for', item.quantity, 'items', '''.
    .
    .''')

    def remove(self):
        item_delete = input("Which item would you like to remove? ")
        item_found = False

        for item in self.items:
            if item.name == item_delete:
                item_found = True
                item_quantity_delete = int(input("How many would you like to delete? "))

                if item.quantity >= item_quantity_delete:
                    item.quantity -= item_quantity_delete
                    print(f"Removed {item_quantity_delete} of {item.name}. Remaining: {item.quantity}")

                    if item.quantity == 0:
                        self.items.remove(item)
                        print(f"{item.name} has been completely removed from the cart.")
                else:
                    print(f"Not enough quantity in cart to remove. Available quantity: {item.quantity}")
                break
        if not item_found:
            print("Invalid item name.")


def main():
    cart = Cart()
    store = Store(items=[Item('apple', .50, 100), Item('banana', .12, 100), Item('eggs', 5, 100)])

    booler = True
    while booler is True:
        prompt = input('''Type add to add to cart, type show cart to show your cart. Type checkout to checkout, 
type remove to remove items from your cart, type show to see available items or type quit to quit ''')
        if prompt == 'remove':
            cart.remove()

        if prompt == 'add':
            cart.add_to_cart(store)

        elif prompt == 'show':
            print(cart.items)

        elif prompt == 'show cart':
            for item in cart.items:
                print(f"Item: {item.name}, Quantity: {item.quantity}")

        elif prompt == 'checkout':
            cart.checkout()
            booler = False

        elif prompt == 'quit':
            print('Thank you for shopping here')
            booler = False


main()

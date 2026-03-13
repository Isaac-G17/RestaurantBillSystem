# Function for calculate consumption
def calculate_consumption(dish_price, drink_price, quantity):
    subtotal = (dish_price + drink_price) * quantity
    return subtotal

# Function for apply tax to consumption
def apply_tax(subtotal):
    tax = subtotal * 0.10
    total = subtotal + tax
    return tax, total

# Function for print restaurant bill
def print_invoice(dish, drink, quantity, subtotal, tax, total):
    print()
    print("----Restaurant Bill----")
    print("Dish:", dish)
    print("Drink:", drink)
    print("Quantity:", quantity)
    print("Subtotal: $", subtotal)
    print("Tax: $", tax)
    print("Total: $", total)
    print("-----------------------")


# program main
dish = input("Enter dish name: ")
dish_price = float(input("Enter dish price $"))

drink = input("Enter drink name: ")
drink_price = int(input("Enter drink price $"))

quantity = int(input("Enter quantity: "))

subtotal = calculate_consumption(dish_price, drink_price, quantity)

tax, total = apply_tax(subtotal)

print_invoice(dish, drink, quantity, subtotal, tax, total)


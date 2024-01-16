menu = {"pizza":3.00,
        "sandwish":2.50,
        "popcorn":6.00,
        "fries":2.50,
        "chips":1.00,
        "pessi":3.00,
        "cola":3.50,
        "lemonade":3.00}
cart = []
total = 0
print("-----MENU-----")
for key, value in menu.items():
    print(f"{key:10} -{value:2f}")
print("--------------")
while True:
    food = input("Enter a food u like to buy(press q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("--Your Order--")
for food in cart:
    total += menu.get(food)
    print(food, end="")
    print()
print(f"Total = ${total}")
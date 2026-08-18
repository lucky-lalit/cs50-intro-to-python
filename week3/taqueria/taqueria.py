def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    result = order(menu)


def order(menu):
    Total = 0
    while True:
        try:
            user_input = input("Item: ").title()
            item_price = menu[user_input]
            Total += item_price
            print(f"Total: ${Total:.2f}")
        except KeyError:
            # print("KeyError")
            pass
        except EOFError:
            print()
            return 0

main()

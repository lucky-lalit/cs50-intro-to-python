# def main():
Amount_due = 50
while Amount_due != 0:
    print(f"Amount Due: {Amount_due}")
    user_input = int(input("Insert Coin: "))
    if user_input != 25 and user_input != 10 and user_input != 5:
        continue
    Amount_due = Amount_due - user_input
    if Amount_due <= 0:
        print(f"Change Owed: {abs(Amount_due)}")
        break

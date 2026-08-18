def main():
    tank_volume = get_fraction()
    if tank_volume <= 1:
         print("E")
    elif tank_volume >= 99:
        print("F")
    else:
        print(f"{tank_volume}%")

def get_fraction():
    while True:
        try:
            x,y = input("Fraction: ").split('/')
            x = int(x)
            y = int(y)
            if x > y or x < 0 or y < 0:
                continue
            return round((x/y) * 100)

        except ValueError:
            print("value Error")
        except ZeroDivisionError:
            print("ZeroDivisionError")
main()

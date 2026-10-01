def main():
    inp = input("Input: ")
    gauge(convert(inp))


def convert(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if (x < 0 or y < 0) and y != 0:
            raise ValueError
        result = round((x/y) * 100)
        # gauge(result)
        return result
    except ValueError:
        # print("value Error")
        raise ValueError
        # exit
    except ZeroDivisionError:
        # print("ZeroDivisionError")
        raise ZeroDivisionError
        # exit


def gauge(percentage):
    if percentage >= 99:
        # {
        # print("F")
        return "F"
        # }
    elif percentage <= 1:
        # {
        # print("E")
        return "E"
        # }
    # print(f"{percentage}%")
    return f"{percentage}%"


if __name__ == "__main__":
    main()

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    dollar = d[1:]
    print(float(dollar))
    return float(dollar)


def percent_to_float(p):
    # TODO
    percent_tip = p[:-1]
    return float(percent_tip) / 100


main()

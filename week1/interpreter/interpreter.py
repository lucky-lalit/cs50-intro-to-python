user_input = input("Expression: ").strip()
x,y,z = user_input.split(" ")


match y:
    case '+':
        value = float(int(x) + int(z))
        print(f"{value:.1f}")
    case '-':
        value = float(int(x) - int(z))
        print(f"{value:.1f}")
    case '*':
        value = float(int(x) * int(z))
        print(f"{value:.1f}")
    case '/':
        value = float(int(x) / int(z))
        print(f"{value:.1f}")

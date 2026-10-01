def main():
    inp = input("Input: ")
    value(inp[:5])

def value(greeting[:5]):
    if 'hello' == greeting.lower():
        return 0
    elif greeting[:1].lower() == 'h':
        return 20
    return 100


if __name__ == "__main__":
    main()

def main():
    inp = input("What's your name ? ")
    hello(inp)

def hello(to = "world"):
    print("debug1",to)
    print("hello, ",to)
    return f"hello, {to}"

if __name__ == "__main__":
    main()

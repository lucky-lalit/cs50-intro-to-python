import validators

def main():
    inp = input("Enter mail? ")
    if validators.email(inp):
        print("valid")
    else:
        print("Invalid")

main()

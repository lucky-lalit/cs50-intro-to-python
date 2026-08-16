user_input = input("Greeting: ")

user_input = user_input.strip()
user_input = user_input[:5]

if 'Hello' == user_input:
    print('$0')
elif user_input[:1] == 'H':
    print("$20")
else:
    print("$100")

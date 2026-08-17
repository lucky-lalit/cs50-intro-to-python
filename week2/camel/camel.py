user_input = input("camelCase: ")
result = ''

for letter in user_input:
    if letter.isupper():
        result += '_' + letter
    else:
        result += letter
print(f"snake_case: {result.lower()}")

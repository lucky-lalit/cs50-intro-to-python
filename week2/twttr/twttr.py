user_input = input("Input: ")
vowels = ['a','e','i','o','u']
result = ''
for letter in user_input:
    if (letter.lower()) not in vowels:
        result += letter
print(result)

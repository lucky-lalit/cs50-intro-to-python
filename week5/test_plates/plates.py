def main():
    inp = input("Input : ")
    isvalid(inp)

def is_valid(s):
    characters = ''
    number = ''
    if len(s) > 6:
        return False
    for index,character in enumerate(s):
        if not character.isdigit() and not character.isalpha():
            return False
        if character.isdigit():
            characters = s[:index]
            number = s[index:]
            break
        elif index + 1 == len(s):
            characters = s
    for letter in characters:
        if not letter.isalpha():
            # print("debug digit")
            return False
    for digit in number:
        # print("debug alpha")
        if not digit.isdigit():
            return False
    if len(characters) != len(s):
        # for letter in character:
        #     if not character.isdigit(letter):
        #         return False
        if len(characters) < 2 or number[0] == '0':
            return False
    else:
        if len(characters) < 2:
            return False
    return True

if __name__ == "__main__":
    main()


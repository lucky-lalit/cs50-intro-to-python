def main():
    inp = input("Input: ")
    shorten(inp)


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for letter in word:
        if (letter.lower()) not in vowels:
            result += letter
    return result


if __name__ == "__main__":
    main()

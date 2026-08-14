def main():
    inp = input()
    converted = convert(inp)
    print(converted)


def convert(string):
    new_str = string.replace(':)', "🙂").replace(':(', "🙁")
    return new_str


main()

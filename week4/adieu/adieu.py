import inflect
def main():
    print(convert())


def convert():
    p = inflect.engine()
    input_tuple = tuple()
    while True:
        try:
            user_input = input("Name: ")
            input_tuple = input_tuple + (user_input,)
            for i in input_tuple:
                print(i)
            # return 'Adieu, adieu, to ' + p.join(input)
        except EOFError:
            print()
            return 'Adieu, adieu, to ' + p.join(input_tuple)


main()

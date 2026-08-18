def main():
    grocery_dict = {}
    while True:
        try:
            input_item = input()
            count = grocery_dict[input_item]
            grocery_dict[input_item] = grocery_dict[input_item] + 1
        except KeyError:
            grocery_dict[input_item] = 1
        except EOFError:
            sorted_dict = sorted(grocery_dict)
            for i in sorted_dict:
                print(grocery_dict[i],i.upper())
            break


main()

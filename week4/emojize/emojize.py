import emoji
def main():
    # import emoji
    user_input = input("Input: ")
    result = converter(user_input)
    print("ouput " + result)



def converter(input):
    return emoji.emojize(input,language='alias')

main()

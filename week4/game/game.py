from random import randint
def main():
    print(guess())




def guess():
    while True:
        try:
            user_input = int(input("Level: "))
            random_input = randint(1,user_input)
            print('random input',random_input)
            if user_input <= 0:
                continue
            while True:
                try:
                    global user_guess
                    user_guess = int(input("Guess: "))
                    if user_guess <= 0:
                        continue
                    if user_guess < random_input:
                        print('Too small!')
                        continue
                    elif user_guess > random_input:
                        print('Too large!')
                        continue
                    break
                except:
                    pass
            # if user_guess < random_input:
            #     print('Too large!')
            # elif user_guess > random_input:
            #     print('Too small!')
            return 'Just right!'
                # continue
        except ValueError:
            pass

main()

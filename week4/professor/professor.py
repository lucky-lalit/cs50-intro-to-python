import random


def main():
    level = get_level()
    count = 0
    # if level == 1:
    #     start = 0
    #     end = 10
    # elif level == 2:
    #     start = 10
    #     end = 100
    # else:
    #     start = 100
    #     end = 1000
    # list_a = []
    # list_b = []
    for i in range(10):
        # while True:
        #     global exist
        #     exist = False
        a = generate_integer(level)
        b = generate_integer(level)
            # if len(list_a) == 0:
            #     list_a.append(a)
            #     list_b.append(b)
            #     break
            # for j in range(len(list_a)):
            #     if list_a[j] == a and b == list_b[j]:
            #         # global exist
            #         exist = True
            #         break
            # if exist:
            #     continue
            # else:
            #     list_a.append(a)
            #     list_b.append(b)
            #     break
        global check
        check = False
        for i in range(3):
            user_answer = int(input(f"{a} + {b} = "))
            if user_answer == a + b:
                # global cout
                # print('inside')
                count = count + 1
                check = True
                break
            else:
                print('EEE')
        if (not check):
            print(f"{a} + {b} = {a+b}")
    print(f"Score: {count}")
    return f"{count}"



def get_level():
    while True:
        try:
            level_input = int(input("Level: "))
            if level_input < 1:
                continue
            if level_input > 3:
                continue
            return level_input
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        start = 0
        end = 10
    elif level == 2:
        start = 10
        end = 100
    else:
        start = 100
        end = 1000
    return random.randint(start,end-1)



if __name__ == "__main__":
    main()

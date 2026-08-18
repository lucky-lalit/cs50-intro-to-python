# print("Hello welcome)?

# x = int(input("what's the value of x? "))
# print(x)

# def main():
#     x = get_int()
#     print(f"x is {x}")
# def get_int():
#     while True:
#         try:
#             return int(input("whats the value? "))
#         except ValueError:
#             pass
#         # print("please enter the integer")

# main()


# temp = {'one':1,'two':2,'three':3}
# result = temp['one']
# print(result)

while True:
        try:
            user_input = input("Date: ").strip()
            MM,DD,YYYY = user_input.split(' ')
            if MM not in months:
                continue
            MM = months.index(MM) + 1
            if DD[-1] == ",":
                DD = int(DD[:-1])
            else:
                continue
            if DD > 31:
                continue
            print(f"{YYYY}-{MM:02}-{DD:02}")
            break
        except ValueError:
            try:
                MM,DD,YYYY = user_input.split('/')
                if len(MM) > 2 or int(DD) > 31 or int(MM) > 12:
                    continue
                print(f"{YYYY}-{int(MM):02}-{int(DD):02}")
                break

# def main():
#     print_meow(get_number())


# def get_number():
#     while True:
#         input_user = int(input("Ente the number: "))
#         if input_user > 0:
#             return input_user

# def print_meow(times):
#     for _ in range(times):
#         print("meow")


# main()

# while True:
#     print("meow")

# print("meow\n" * 3,end = '')

# students = ["Hermione", "Harry", "Ron"]

# for student in students:
    # print(student)

# for i in range(len(students)):
    # print(i+1,students[i])

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# for student in students:
#     print(student,students[student],sep = ', ')

# for i,value in enumerate(students):
#     print(i+1,students[value])


# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None},
# ]


# for student in students:
#     print(student["name"],student["house"],student["patronus"],sep = ", ")


# def main():
#     print_column(get_number())
#     print_row(get_number())


# def get_number():
#     while True:
#         input_user = int(input("Ente the number: "))
#         if input_user > 0:
#             return input_user

# def print_column(number):
#     print('#\n' * number,end ='')

# def print_row(number):
#     print("#" * number)

# main()

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for k in range(size):
            print("#",end="")
        print()

main()

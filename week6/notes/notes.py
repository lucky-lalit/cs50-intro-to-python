# name = input("What's your name ? ")
# file = open("names.txt","a")
# file.write(f"{name}\n")
# file.close()


# name = input("what's your name ? ")
# with open("names.txt","r") as file:
    # file.write(f"{name}\n")
    #  lines = file.readlines()
    # for line in file:
        # print("hello,",line.rstrip())

# for line in lines:
    # print("hello,", line.rstrip())

# names = []

# with open("names.txt","r") as file:
    # for line in file:
        # names.append(line.rstrip())

# for name in sorted(names):
    # print("Hello,",name)
# students = []
# with open("names.csv","r") as file:
    # for line in file:
        # name = line.rstrip().split(",")
        # print(name)
        # student = {"name" : name[0], "house" : name[1]}
        # student["name"] = name[0]
        # student["house"] = name[1]
        # students.append(student)
        # students.append(f"{name[0]} lives in {name[1]}")
        # print(f"{name[0]} lives in {name[1]}")
# for student in sorted(students):
    # print(student)
# for student in students:
    # print(f"{student['name']} is in {student['house']}")

# students = []

# with open("names.csv","r") as file:
#     for line in file:
#         name,house = line.rstrip().split(",")
#         students.append({"name" : name, "house" : house})
        # print(students)

# def get_name(student):
#     return student["house"]

# for student in sorted(students, key=get_name):
    # print(f"{student['name']} is in {student['house']}")


# students = []

# with open("names.csv","r") as file:
#     for line in file:
#         name,home = line.rstrip().split(",")
#         students.append({"name" : name, "home" : home})

# for student in sorted(students,key = lambda student : student['name']):
#     print(f"{student['name']} is in {student['home']}")

# import csv
# students = []

# with open("names.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
        # print(f"{row[0]} lives in {row[1]}")
#         students.append({"name" : row[0], "home" : row[1]})

# for student in sorted(students,key = lambda student : student['name']):
#     print(f"{student['name']} is in {student['home']}")


# import csv
# students = []

# with open("names.csv","r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name" : row["name"], "home" : row["home"]})

# for student in sorted(students,key = lambda student : student['name']):
#     print(f"{student['name']} is in {student['home']}")


# import csv

# name = input("what's the name ? ")
# home = input("where you live ? ")

# with open("students.csv","a") as file:
#         writer = csv.DictWriter(file,fieldnames = ["name","home"])
#         writer.writerow({"name":name, "home":home})



# import sys

# from PIL import Image

# images = []
# for arg in sys.argv[1:]:
#     image = Image.open(arg)
#     images.append(image)

# images[0].save("costumes.gif", save_all = True, append_images = [images[1]], duration = 200, loop = 0)





# def main():
#     # name = get_name()
#     # name, house = get_student()
#     # print(f"{name} from {house}")
#     student = get_student()
#     if student["name"] == "lalit":
#         student["name"] = 'amar'
#     print(f"{student['name']} from {student['house']}")


# def get_student():
#     # student = {}
#     # student["name"] = input("Name: ")
#     # student["house"] = input("House: ")
#     return {"name" : input("Name: "), "house" : input("House: ")}

# # def get_name():
#     # return input("Name: ")

# # def get_hosue():
#     # return input("House: ")

# if __name__ == "__main__":
#     main()



# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     # getter for house
#     @property
#     def house(self):
#         return self._house
#     # setter for hosue
#     @house.setter
#     def house(self,house):
#         if house not in ["Mumbai","Pune","Kolhapur","Navi-Mumbai","Nagpur"]:
#             raise ValueError("Missing House")
#         self._house = house

#     @property
#     def name(self):
#         return self._name

#     def name(self,name):
#         if not name:
#             raise ValueError("Missing Name")
#         self.name = name



# def main():
#     student = get_student()
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name,house)

# if __name__ == "__main__":
#     main()


# import random

# class Hat:
#     # def __init__(self):
#     houses = ["Mumbai","Pune","Kolhapur"]
#     @classmethod
#     def sort(cls,name):
#         print(name,"is in",random.choice(cls.houses))

# # house = Hat()
# Hat.sort("Lalit")


class Wizard:
    def __init__(self,name):
        self.name = name

# class Student(Wizard):
#     def __init__(self,name,house):
#         super().__init__(name)
#         # self.name = name
#         self.house = house

# class Professor(Wizard):
#     def __init__(self,name,subject):
#         super().__init__(name)
#         self.subject = subject


# wizard = Wizard("Lalit")
# student = Student("Amar","Mumbai")
# professor = Professor("Ram","17/237")



class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        print("add  ")
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)

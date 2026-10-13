class Package:
    def __init_(self,number,sender,receiver,weight):
        self.number = number
        self.sender = sender
        self.receiver = receiver
        self.weight = weight


def main():
    packages = [Package(1,"bob","charlie",10),
    Package(2,"alice","drek",40)]

    main()


# class Food:

#     base_hearts = 2
#     def __init__(self,ingredients):
#         self.ingredients = ingredients
#         self.hearts = Food.calculate_items(ingredients)

#     @classmethod
#     def calculate_items(cls,ingredients):
#         hearts = cls.base_hearts
#         for i in ingredients:
#             if "hearty" in i.lower():
#                 hearts += 2
#             else:
#                 hearts += 1
#         return hearts


#     @classmethod
#     def from_nothing(cls,hearts):
#         food = cls(ingredients = [])
#         food.hearts = hearts
#         return food

# def main():
#     result = Food(ingredients = ["apple","hearty mushroom"])
#     print(f"the result for ingredients is {result.hearts} hearts!!")

#     result = Food.from_nothing(hearts=2)
#     print(f"the result for ingredients is {result.hearts} hearts!!")



# main()

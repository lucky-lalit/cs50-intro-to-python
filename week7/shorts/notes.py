import re

# def main():
#     code = input("Hexadecimal color code: ")

#     pattern = r"^#[a-fA-F0-9]{6}$"
#     if match := re.search(pattern,code):
#         print(f"valid matched with {match.group()}")
#     else:
#         print("Invalid")


# main()

locations = {"+1":"United states and Canada", "+505":"Nicaragua", "+62":"Indonesia"}

def main():
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}$"
    number = input("Number: ")
    if match := re.search(pattern,number):
        num = match.group("country_code")
        # print(num)
        print(f"valid {locations[num]}")
    else:
        print("Invalid")


main()

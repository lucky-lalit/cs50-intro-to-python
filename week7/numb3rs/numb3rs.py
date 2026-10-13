import re
import sys


def main():
    result = validate(input("IPv4 Address: "))
    print(result)


# def validate(ip):
#     match = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
#     try:
#         if int(match.group(1)) > 255 or int(match.group(2)) > 255 or int(match.group(3)) > 255 or int(match.group(4)) > 255:
#             return False
#     except AttributeError:
#         return False
#     return True

def validate(ip):
    try:
        if match := re.search(r"^(([0-9]|[1-9][0-9]|1[0-9][0-9])|(2[0-4][0-9])|(2[5][0-5]))\.(([0-9]|[1-9][0-9]|1[0-9][0-9])|(2[0-4][0-9])|(2[5][0-5]))\.(([0-9]|[1-9][0-9]|1[0-9][0-9])|([2][0-4][0-9])|([2][5][0-5]))\.(([0-9]|[1-9][0-9]|1[0-9][0-9])|([2][0-4][0-9])|([2][5][0-5]))$", ip):
            return True
    except AttributeError:
        return False
    return False


if __name__ == "__main__":
    main()

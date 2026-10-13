# email = input("Enter email address ").strip()

# username, domain = email.split('@')

# if '@' in email and '.' in email:
# if username and '.' in domain:
# if username and domain.endswith('.edu'):
#     print("Valid")
# else:
#     print("Invalid")


import re

# email = input("what the email ?").strip()

# if re.search(r"^\w+@(\w+\.)?\w+\.(edu|gov|net|org|com)$",email,re.IGNORECASE):
#     print("valid")
# else:
#     print("Invalid")


# name = input("what's your name ?").strip()
# if matches := re.search(r"^(.+), *(.+)$", name):
# if ',' in name:
    # last, first = name.split(', ')
# if matches:
    # last, first = matches.groups()
    # last = matches.group(1)
    # first = matches.group(2)
    # name = matches.group(2) + " " + matches.group(1)

# print(f"hello, {name}")


# url = input("URL: ").strip()
# # username = url.removeprefix("https://twitter.com/")
# username = re.search(r"^https?://(www\.)?twitter.com/(.+)$","",url)
# if username:
#     print(f"username: {username.group(2)}")


import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

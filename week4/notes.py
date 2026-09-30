# from random import choice

# result = choice(["Head","Tail"])
# print(result)


    # from random import randint

    # result = randint(1,10)
    # print(result)

# from random import shuffle

# operation = ["Male","Female","Tuntun_Mossi"]
# shuffle(operation)
# for i in operation:
#     print(i)

# from statistics import mean

# print(mean([20,20,20,20,20]))

import sys
try:
    print("helo welcome to jungle",float(sys.argv[1])
except IndexError:
    print("please enter valid Commnad line")

# if (len(sys.argv) < 2):
#     sys.exit("too few arguments")
# elif (len(sys.argv) > 2):
#     sys.exit("too many arguments")
# for i in sys.argv[1:]:
    # print("hello",i)

# import cowsay

# if len(sys.argv) == 2:
#     cowsay.trex("Hello, " + sys.argv[1])


# import requests
# import json

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent = 2))
# print(response)
# print(response.json())
# o = response.json()
# for result in o["results"]:
    # print(result["trackName"])


# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# o = response.json()
# for result in o["results"]:
#     print(result["trackName"])


# def hello(name):
#     print(f"hello, {name}")


# def goodbye(name):
#     print(f"goodbye, {name}")

# import random
# print(random.randint(0,100,))
# x,y = random.randint(1,9),random.randint(1,5)
# print(x,y)

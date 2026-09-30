import sys
import requests
import json


try:
    conversion = float(sys.argv[1])
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=a1ff5b4044879a2597d3d1c584eb13aa2206b188647b3525737a4b2740f338da")
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit()

# response = requests.get("https://rest.coincap.io/v3/price/bysymbol/BTC?apiKey=a1ff5b4044879a2597d3d1c584eb13aa2206b188647b3525737a4b2740f338da")
result = response.json()
# print(result["data"]["priceUsd"])
# print(json.dumps(response.json(), indent = 2))
# for i in result["data"]:
    # {
        # if (i == "priceUsd"):
        # print(i["priceUsd"])
    # }
amount = float(result["data"]["priceUsd"]) * conversion
# for price in result["data"]:
    # print(f"* {price["priceUsd"]}")
print(f"${amount:,.4f}")



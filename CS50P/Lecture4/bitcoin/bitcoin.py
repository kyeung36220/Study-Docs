import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Not enough arguments")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    o = response.json()

    btc_value = str(o["bpi"]["USD"]["rate"]).replace(',',"")

    total = float(sys.argv[1]) * float(btc_value)

    print("$", f'{round(total,4):,}', sep="")


except requests.RequestException:
    sys.exit("Error")

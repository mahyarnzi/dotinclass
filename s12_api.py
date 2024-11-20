# import requests
#
# url = "https://api.restful-api.dev/objects"
#
# payload={}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
# for item in response.json():
#     print(item["name"])


# import requests
#
# url = "https://api.restful-api.dev/objects"
# params = {"id": ["3","4"],
#           "name": "Apple iPhone 12 Pro Max"}
#
#
# payload = {}
# headers = {}
#
# response = requests.request("GET", url, params=params, headers=headers, data=payload)
# print(response.url)
# print(response.json())


# import requests
# import json
#
# url = "https://api.restful-api.dev/objects/ff80818192925da70192dc689c04260b"
#
# payload = json.dumps({
#     "name": "Asghar-Camera",
#     "data": {
#         "year": 2024,
#         "price": 2000,
#         "CPU model": "Intel Core i9",
#         "Hard disk size": "1 TB"
#     }
# })
# headers = {
#     'Content-Type': 'application/json'
# }
#
# response = requests.request("PUT", url, headers=headers, data=payload)
#
# print(response.status_code)
# print(response.json())


import requests
import time

def get_btc_usdt():
    url = "https://api.nobitex.ir/market/stats?srcCurrency=btc&dstCurrency=usdt"

    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.json()
    print(result['stats']['btc-usdt']['latest'])

while True:
    get_btc_usdt()
    time.sleep(10)

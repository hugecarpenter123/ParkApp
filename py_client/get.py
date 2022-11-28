import requests
import json

endpoint = 'http://127.0.0.1:8000/api/locations/'

def get_method():
    endpoint = 'http://127.0.0.1:8000/api/locations/'
    key = input("Give key: ")
    value = input('Give value: ')
    if key and value:
        endpoint += '?{}={}'.format(key, value)
    get_response = requests.get(endpoint)
    print(get_response)
    # print(get_response.json())

# to samo -------------------
# try:
#     # get_response = requests.get(endpoint, params={"warzywo": "kapusta"}, json={"karwasz": "twarz"})
#     get_response = requests.get(endpoint)
#     print(get_response)
#     # print(json.loads(get_response.content))
#     print(get_response.json())
# except:
#     print("Something went wrong")
# ---------------------------
get_method()

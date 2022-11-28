import requests
import json

endpoint = 'http://127.0.0.1:8000/api/locations/'

def get_method():
    endpoint = 'http://127.0.0.1:8000/api/statistics/'
    pk = input("Location pk: ")
    if pk:
        endpoint += pk
    get_response = requests.get(endpoint)
    print(get_response)
    print(get_response.json())

get_method()
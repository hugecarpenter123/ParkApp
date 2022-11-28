import requests
import json

def get_method():
    location_pk = input("Give pk: ")
    endpoint = 'http://127.0.0.1:8000/api/list/%s' % location_pk
    get_response = requests.get(endpoint)
    print(get_response)
    print(get_response.json())

def put_method():
    detail_pk = input("Give pk: ")
    status = input("Give status: ")
    endpoint = 'http://127.0.0.1:8000/api/update/%s' % detail_pk

    data = {}
    data['status'] = status
    put_response = requests.put(endpoint, json=data)
    print(put_response)
    print(put_response.json())

request_type = input("request_type: ")
if request_type.casefold() == "get":
    get_method()
elif request_type == "put":
    put_method()
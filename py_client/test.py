import requests
import json
import random
import time

def get_method(location_pk):
    endpoint = 'http://127.0.0.1:8000/api/list/%s' % location_pk
    get_response = requests.get(endpoint)
    # print(get_response)
    # print(get_response.json())
    return get_response.json()

def put_method(detail_pk, status):
    endpoint = 'http://127.0.0.1:8000/api/update/%d' % detail_pk
    data = {}
    data['status'] = status
    put_response = requests.put(endpoint, json=data)
    print(put_response)
    print(put_response.json())

def modify_random(id_set):
    time_span = range(2,7)
    choice_span = range(1, len(id_set) + 1)
    status = ['free', 'occupied']
    while True:
        sleep_time = random.choice(time_span)
        # print("sleep time:", sleep_time)
        time.sleep(sleep_time)
        for i in range(random.choice(choice_span)):
            put_method(random.choice(id_set), status=random.choice(status))
            # print('modify_random({}, {})'.format(random.choice(id_set), random.choice(status)))




all_data = get_method(1)
upper = all_data['section_qs'][0]['spot_qs']
# print(upper)
# id_set = [x['id'] for x in upper]
# print("id_set:", id_set)
# modify_random(id_set)

HUGEEEE_ID_SET = []
for i in range(1,5):
    all_data = get_method(i)
    for section in all_data['section_qs']:
        # print(section['spot_qs'])
        id_set = [x['id'] for x in section['spot_qs']]
        HUGEEEE_ID_SET += id_set

modify_random(HUGEEEE_ID_SET)

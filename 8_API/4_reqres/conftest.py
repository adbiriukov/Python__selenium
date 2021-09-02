import pytest
import requests
import json

# @pytest.fixture()
# def api_client_get_status(api_request):
#     r = requests.get("https://reqres.in/"+str(api_request[0])+"")
#     # this make dict
#     # r = r.json()
#     r = r.status_code
#     return r == api_request[1]


# @pytest.fixture()
# def api_client_get_value(api_request):
#     r = requests.get("https://reqres.in/"+str(api_request[0])+"")
#     response_body = r.json()
#     return response_body

@pytest.fixture()
def api_client_post_value(api_request, json_request):
    # json_request = json_request[0]
    print("=============")
    print(json_request)
    # print(type(json_request))
    # json_request = json.dumps(json_request)
    # print("+++++++++")
    # print(json_request)
    # print(type(json_request))
    r = requests.post("https://reqres.in/"+str(api_request)+"", json={json_request})
    response_body = r.json()
    return response_body



# print('response.headers == ' + str(response.headers["Content-Type"]))  # application/json; charset=utf-8

# def api_client(api_request, json_request):
# r = requests.post("https://reqres.in/"+str(api_request)+"", json={json_request})

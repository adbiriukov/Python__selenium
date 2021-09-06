import requests
import pytest


# To get status code
@pytest.fixture()
def api_client_get_status(api_request):
    r = requests.get("https://gorest.co.in/"+str(api_request[0])+"")
    r = r.status_code
    return r


# # To get value
@pytest.fixture()
def api_client_get_value(api_request):
    r = requests.get("https://jsonplaceholder.typicode.com/"+str(api_request[0])+"")
    r = r.json()
    return r


# To post
@pytest.fixture()
def api_client_post(api_request, json_request, headers):
    r = requests.post("https://gorest.co.in/"+str(api_request)+"", json_request, headers)
    return r.json()

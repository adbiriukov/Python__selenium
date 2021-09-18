import requests
import pytest


# to post auth and get status code
@pytest.fixture()
def api_auth_post(api_request, json_request, headers):
    # r = requests.get("https://"+str(login_pass)+"@restful-booker.herokuapp.com/"+str(api_request[0])+"")
    r = requests.post("https://restful-booker.herokuapp.com/"+str(api_request[0])+"", json_request, headers)
    r = r.status_code
    return r

# # # To get value
@pytest.fixture()
def api_client_get_value(api_request, json_request):
    r = requests.get("https://restful-booker.herokuapp.com/"+str(api_request[0])+"", json_request)
    r = r.json()
    return r

# # To post
@pytest.fixture()
def api_client_post(api_request, json_request):
    r = requests.post("https://restful-booker.herokuapp.com/"+str(api_request)+"", data=json_request)
    r = r.status_code
    return r

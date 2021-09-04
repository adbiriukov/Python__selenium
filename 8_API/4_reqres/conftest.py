import pytest
import requests
# import json


@pytest.fixture()
def api_client_get_status(api_request):
    r = requests.get("https://reqres.in/"+str(api_request[0])+"")
    # this make dict
    # r = r.json()
    r = r.status_code
    return r == api_request[1]


@pytest.fixture()
def api_client_get_value(api_request):
    r = requests.get("https://reqres.in/"+str(api_request[0])+"")
    response_body = r.json()
    return response_body


# CREATE
@pytest.fixture()
def api_client_post_value(api_request, json_request):
    r = requests.post("https://reqres.in/"+str(api_request)+"", json_request)
    response_body = r.json()
    return response_body


# UPDATE by PUT
@pytest.fixture()
def api_client_put(api_request, json_request):
    r = requests.put("https://reqres.in/"+str(api_request)+"", json_request)
    response_body = r.json()
    print(response_body)
    return response_body


# UPDATE by PATCH
@pytest.fixture()
def api_client_patch(api_request, json_request):
    r = requests.patch("https://reqres.in/"+str(api_request)+"", json_request)
    response_body = r.json()
    print(response_body)
    return response_body


# DELETE
@pytest.fixture()
def api_client_patch(api_request):
    r = requests.delete("https://reqres.in/"+str(api_request)+"")
    return r.status_code


# REGISTER - SUCCESSFUL
@pytest.fixture()
def api_client_register(api_request, json_request):
    r = requests.post("https://reqres.in/"+str(api_request)+"", json_request)
    response_body = r.json()
    return response_body


# REGISTER - UNSUCCESSFUL
@pytest.fixture()
def api_client_unsuccessful_register(api_request, json_request):
    r = requests.post("https://reqres.in/"+str(api_request)+"", json_request)
    response_body = r.json()
    return response_body


# LOGIN - SUCCESSFUL
@pytest.fixture()
def api_client_login(api_request, json_request):
    r = requests.post("https://reqres.in/"+str(api_request)+"", json_request)
    response_body = r.json()
    return response_body


# LOGIN - UNSUCCESSFUL
@pytest.fixture()
def api_client_login_fail(api_request, json_request):
    r = requests.post("https://reqres.in/"+str(api_request)+"", json_request)
    response_body = r.json()
    return response_body

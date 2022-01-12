import requests
import pytest


@pytest.fixture()
def api_get(api_request, headers):
    r = requests.get("https://petstore.swagger.io/"+str(api_request[0])+"", headers)
    return r.status_code


@pytest.fixture()
def api_post(api_request, data, headers):
    r = requests.post("https://petstore.swagger.io/"+str(api_request[0])+"", json=data, headers=headers)
    return r.json()


@pytest.fixture()
def api_delete(api_request, headers):
    r = requests.delete("https://petstore.swagger.io/"+str(api_request[0])+"", headers)
    return r.status_code


@pytest.fixture()
def api_put(api_request, data, headers):
    r = requests.put("https://petstore.swagger.io/"+str(api_request[0])+"", json=data, headers=headers)
    return r.json()

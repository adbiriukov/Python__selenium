import pytest


# Get status
@pytest.mark.parametrize('api_request', [['api/users?page=2', '201'], ['api/users/2', '201'],
                                         ['api/users/23', '404'], ['api/unknown', '200'],
                                         ['https://reqres.in/api/unknown/2', '201'], ['api/unknown/23', '404']])
def test_api_get_status(api_client_get_status, api_request):
    response = api_client_get_status
    if response is True:
        assert True


# Get value from the list of users
@pytest.mark.parametrize('api_request', [['api/users?page=2', "data", '0', 'id', '7'],
                                         ['api/users?page=2', "data", '0', 'email', 'michael.lawson@reqres.in'],
                                         ['api/users?page=2', "data", '0', 'first_name', 'Michael'],
                                         ['api/users?page=2', "data", '0', 'last_name', 'Lawson'],
                                         ['api/users?page=2', "data", '0', 'avatar',
                                          'https://reqres.in/img/faces/7-image.jpg'],
                                         ['api/users?page=2', "data", '1', 'id', '8']
                                         ])
def test_api_get_value(api_client_get_value, api_request):
    api_response = api_client_get_value
    try:
        int(api_request[4])
        assert api_response[api_request[1]][int(api_request[2])][api_request[3]] == int(api_request[4])
    except ValueError:
        assert api_response[api_request[1]][int(api_request[2])][api_request[3]] == api_request[4]


# CREATE
@pytest.mark.parametrize('api_request', ['api/users'])
@pytest.mark.parametrize('json_request', [{"name": "morpheus", "job": "leader"},
                                          {"name": "Neo", "job": "Chosen one"}])
def test_api_post(api_client_post_value, api_request, json_request):
    api_response = api_client_post_value
    assert api_response["name"] == json_request["name"]
    assert api_response["job"] == json_request["job"]


#  UPDATE by PUT
@pytest.mark.parametrize('api_request', ['api/users'])
@pytest.mark.parametrize('json_request', [{"name": "morpheus", "job": "zion resident"}])
def test_api_put(api_client_put, api_request, json_request):
    api_response = api_client_put
    assert api_response["name"] == json_request["name"]
    assert api_response["job"] == json_request["job"]


# UPDATE by PATCH
@pytest.mark.parametrize('api_request', ['api/users'])
@pytest.mark.parametrize('json_request', [{"name": "morpheus", "job": "zion resident"}])
def test_api_patch(api_client_patch, api_request, json_request):
    api_response = api_client_patch
    assert api_response["name"] == json_request["name"]
    assert api_response["job"] == json_request["job"]


# DELETE
@pytest.mark.parametrize('api_request', ['api/users'])
def test_api_patch(api_client_patch, api_request):
    api_response = api_client_patch
    assert api_response == 204


# REGISTER - SUCCESSFUL
@pytest.mark.parametrize('api_request', ['api/register'])
@pytest.mark.parametrize('json_request', [{"email": "eve.holt@reqres.in", "password": "pistol"}])
def test_api_register_successful(api_client_register, api_request, json_request):
    api_response = api_client_register
    assert api_response["token"] == 'QpwL5tke4Pnpja7X4'


# REGISTER - UNSUCCESSFUL
@pytest.mark.parametrize('api_request', ['api/register'])
@pytest.mark.parametrize('json_request', [{"email": "sydney@fife"}])
def test_api_unsuccessful_register(api_client_unsuccessful_register, api_request, json_request):
    api_response = api_client_unsuccessful_register
    assert api_response["error"] == 'Missing password'


# LOGIN - SUCCESSFUL
@pytest.mark.parametrize('api_request', ['api/login'])
@pytest.mark.parametrize('json_request', [{"email": "eve.holt@reqres.in", "password": "cityslicka"}])
def test_api_login_successful(api_client_login, api_request, json_request):
    api_response = api_client_login
    assert api_response["token"] == 'QpwL5tke4Pnpja7X4'


# LOGIN - UNSUCCESSFUL
@pytest.mark.parametrize('api_request', ['api/login'])
@pytest.mark.parametrize('json_request', [{"email": "peter@klaven"}])
def test_api_login_successful(api_client_login_fail, api_request, json_request):
    api_response = api_client_login_fail
    assert api_response["error"] == 'Missing password'

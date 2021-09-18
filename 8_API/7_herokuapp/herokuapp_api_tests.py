import pytest


# # auth and get status
# @pytest.mark.parametrize('api_request', [['auth', '200']])
# @pytest.mark.parametrize('json_request', [{'method': 'POST', 'username': 'admin', 'password': 'password123'}])
# @pytest.mark.parametrize('headers', [{'Content-type': 'application/json'}])
# def test_api_auth_post(api_auth_post, api_request, json_request, headers):
#     r = api_auth_post
#     print('==========')
#     print(r)
#     assert r == int(api_request[1])

# # auth by token
# @pytest.mark.parametrize('api_request', [['auth', '200']])
# @pytest.mark.parametrize('json_request', [{'method': 'POST', 'token': 'abc123'}])
# @pytest.mark.parametrize('headers', [{'Content-type': 'application/json'}])
# def test_api_auth_post(api_auth_post, api_request, json_request, headers):
#     r = api_auth_post
#     print('==========')
#     print(r)
#     assert r == int(api_request[1])


# @pytest.mark.parametrize('api_request', [['booking']])
# @pytest.mark.parametrize('json_request', [{'method': 'GET', 'firstname': 'Sally'}])
# def test_api_get_value(api_client_get_value, api_request, json_request):
#     r = api_client_get_value
#     print(r)

# to get specific booking
# @pytest.mark.parametrize('api_request', [['booking/1']])
# @pytest.mark.parametrize('json_request', [{'method': 'GET', 'lastname': 'Brown'}])
# def test_api_get_value(api_client_get_value, api_request, json_request):
#     r = api_client_get_value
#     print(r)

# Create booking
@pytest.mark.parametrize('api_request', [['booking/1']])
@pytest.mark.parametrize('json_request', [{
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}])
@pytest.mark.parametrize('headers', [{'Content-type': 'application/json'}])
def test_api_get_value(api_client_post, api_request, json_request, headers):
    r = api_client_post
    print(r)

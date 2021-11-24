import pytest


# auth and get status
@pytest.mark.parametrize('api_request', [['v2/pet', '200']])
@pytest.mark.parametrize('json_request', [{'method': 'POST', "id": 0,
                                           "category": {
                                               "id": 0,
                                               "name": "string"
                                           },
                                           "name": "doggie",
                                           "photoUrls": [
                                               "string"
                                           ],
                                           "tags": [
                                               {
                                                   "id": 0,
                                                   "name": "string"
                                               }
                                           ],
                                           "status": "available"}])
@pytest.mark.parametrize('headers', [{'Content-type': 'application/json'}])
def test_api_auth_post(api_auth_post, api_request, json_request, headers):
    r = api_auth_post
    print('==========')
    print(r)
    assert r == int(api_request[1])

# # auth by token
# @pytest.mark.parametrize('api_request', [['auth', '200']])
# @pytest.mark.parametrize('json_request', [{'method': 'POST', 'token': 'abc123'}])
# @pytest.mark.parametrize('headers', [{'Content-type': 'application/json'}])
# def test_api_auth_post(api_auth_post, api_request, json_request, headers):
#     r = api_auth_post
#     print('==========')
#     print(r)
#     assert r == int(api_request[1])
#
#
# @pytest.mark.parametrize('api_request', [['booking']])
# @pytest.mark.parametrize('json_request', [{'method': 'GET', 'firstname': 'Sally'}])
# def test_api_get_value(api_client_get_value, api_request, json_request):
#     r = api_client_get_value
#     print(r)
#
#
# # to get specific booking
# @pytest.mark.parametrize('api_request', [['booking/1']])
# @pytest.mark.parametrize('json_request', [{'method': 'GET', 'lastname': 'Brown'}])
# def test_api_get_value(api_client_get_value, api_request, json_request):
#     r = api_client_get_value
#     print(r)
#
#
# # Create booking
# def test_api_greate_booking(api_client_post):
#     r = api_client_post
#     print(r)
#
#
# # Update booking
# def test_api_put(api_client_put):
#     r = api_client_put
#     print(r)
#
#
# # Remove booking
# def test_remove_booking(remove_booking):
#     r = remove_booking
#     print(r)

import pytest


# @pytest.mark.parametrize('api_request', [['v2/store/inventory', '200']])
# @pytest.mark.parametrize('headers', [{'accept': 'application/json'}])
# def test_get_pet(api_get_pet, api_request, headers):
#     r = api_get_pet
#     print('==========')
#     print(r)
#     assert r == int(api_request[1])


@pytest.mark.parametrize('api_request', [['v2/store/order']])
@pytest.mark.parametrize('header', [{'Content-Type': 'application/json', 'accept': 'application/json'}])
@pytest.mark.parametrize('data', [{
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2021-11-25T14:54:06.445Z",
  "status": "placed",
  "complete": True
}])
def test_api_auth_post(api_post_order, api_request, data, header):
    r = api_post_order
    print('==========')
    print(r['complete'])
    assert r['complete'] is True

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

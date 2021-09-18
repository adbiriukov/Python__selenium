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

# auth by token
@pytest.mark.parametrize('api_request', [['auth', '200']])
@pytest.mark.parametrize('json_request', [{'method': 'POST', 'token': 'abc123'}])
@pytest.mark.parametrize('headers', [{'Content-type': 'application/json'}])
def test_api_auth_post(api_auth_post, api_request, json_request, headers):
    r = api_auth_post
    print('==========')
    print(r)
    assert r == int(api_request[1])


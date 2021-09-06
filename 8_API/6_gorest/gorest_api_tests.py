import pytest


# Get status
@pytest.mark.parametrize('api_request', [['public/v1/users', '200'], ['public/v1/posts', '200'],
                                         ['public/v1/comments', '200'], ['public/v1/todos', '200']
                                         ])
def test_api_get_status(api_client_get_status, api_request):
    r = api_client_get_status
    assert r == int(api_request[1])


# Get posts for 1 user
@pytest.mark.parametrize('api_request', [['public/v1/users', 6, 'name', 'Kurtis Weissnat', 'email',
                                          'Telly.Hoeger@billy.biz', 'address', 'street', 'Rex Trail']])
def test_api_get_value(api_client_get_value, api_request):
    r = api_client_get_value
    # print(r[api_request[1]][api_request[2]])
    # print(r[api_request[1]][api_request[4]])
    # print(r[api_request[1]][api_request[6]][api_request[7]])
    assert r[api_request[1]][api_request[2]] == api_request[3]
    assert r[api_request[1]][api_request[4]] == api_request[5]
    assert r[api_request[1]][api_request[6]][api_request[7]] == api_request[8]

# Post
@pytest.mark.parametrize('api_request', ['public/v1/users'])
@pytest.mark.parametrize('json_request', [{"name": "Tenali Ramakrishna", "gender": "male",
                                           "email": "tenali.ramakrishna@15ce.com", "status": "active"}])
@pytest.mark.parametrize('headers', [{'Authorization: Bearer ACCESS-TOKEN'}])
def test_api_post(api_client_post, api_request, json_request, headers):
    r = api_client_post
    assert r['data']['message'] == 'Authentication failed'

import pytest


# Get status
@pytest.mark.parametrize('api_request', [['posts/1', '200'], ['posts/2', '200']])
def test_api_get_status(api_client_get_status, api_request):
    r = api_client_get_status
    assert r == int(api_request[1])


# Get posts for 1 user
@pytest.mark.parametrize('api_request', [['posts/1', '1', '1',
                                          'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'],
                                         ['posts/2', '1', '2', 'qui est esse']])
def test_api_get_value(api_client_get_value, api_request):
    r = api_client_get_value
    assert r['userId'] == int(api_request[1])
    assert r['id'] == int(api_request[2])
    assert r['title'] == api_request[3]


# Get posts for all users
@pytest.mark.parametrize('api_request', [['posts', '7', '1', '8', 'dolorem dolore est ipsam'], ['posts', '42', '5',
                                                                                                '43', 'eligendi iste nostrum consequuntur adipisci praesentium sit beatae perferendis']])
def test_api_get_value_list(api_client_get_value, api_request):
    r = api_client_get_value
    assert r[int(api_request[1])]['userId'] == int(api_request[2])
    assert r[int(api_request[1])]['id'] == int(api_request[3])
    assert r[int(api_request[1])]['title'] == api_request[4]


# Post
@pytest.mark.parametrize('api_request', ['posts'])
@pytest.mark.parametrize('json_request', [{'method': 'POST', 'title': 'foo', 'body': 'bar', 'userId': '1'}])
@pytest.mark.parametrize('headers', [{'Content-type': 'application/json; charset=UTF-8'}])
def test_api_post(api_client_post, api_request, json_request, headers):
    r = api_client_post
    assert r['title'] == json_request['title']
    assert r['body'] == json_request['body']
    assert r['userId'] == json_request['userId']
    assert r['id'] == 101


# Delete
@pytest.mark.parametrize('api_request', ['/posts'])
@pytest.mark.parametrize('json_request', [{'method': 'DELETE'}])
def test_api_delete(api_client_delete, api_request, json_request):
    r = api_client_delete
    assert r['method'] == 'DELETE'
    assert r['id'] == 101


# PUT
@pytest.mark.parametrize('api_request', ['posts'])
@pytest.mark.parametrize('json_request', [{'method': 'PUT', 'title': 'foo1', 'body': 'bar', 'userId': '1'}])
@pytest.mark.parametrize('headers', [{'Content-type': 'application/json; charset=UTF-8'}])
def test_api_post(api_client_post, api_request, json_request, headers):
    r = api_client_post
    assert r['title'] == json_request['title']
    assert r['body'] == json_request['body']
    assert r['userId'] == json_request['userId']
    assert r['id'] == 101


# PATCH
@pytest.mark.parametrize('api_request', ['posts'])
@pytest.mark.parametrize('json_request', [{'method': 'PATCH', 'title': 'foo1', 'body': 'bar', 'userId': '1'}])
@pytest.mark.parametrize('headers', [{'Content-type': 'application/json; charset=UTF-8'}])
def test_api_post(api_client_post, api_request, json_request, headers):
    r = api_client_post
    assert r['title'] == json_request['title']
    assert r['body'] == json_request['body']
    assert r['userId'] == json_request['userId']
    assert r['id'] == 101


# Filtering resources
@pytest.mark.parametrize('api_request', ["posts?userId=1"])
def test_api_get_value_list(api_client_get_value, api_request):
    r = api_client_get_value
    assert len(r) == 10


# Listing nested resources
@pytest.mark.parametrize('api_request', [["posts/1/comments", '0', 'id labore ex et quam laborum'],
                                         ["albums/1/photos", '1', 'https://via.placeholder.com/600/771796'],
                                         ["users/1/albums", 4, 'eaque aut omnis a'],
                                         ["users/1/todos", 12, 'et doloremque nulla'],
                                         ["users/1/posts", 9, 'optio molestias id quia eum']
                                         ])
def test_api_get_value_list(api_client_get_value, api_request):
    r = api_client_get_value
    if api_request[0] == 'posts/1/comments':
        assert r[int(api_request[1])]['name'] == api_request[2]
    elif api_request[0] == 'albums/1/photos':
        assert r[int(api_request[1])]['url'] == api_request[2]
    else:
        assert r[api_request[1]]['title'] == api_request[2]

import pytest


# create new user
@pytest.mark.parametrize('api_request', [['v2/user', '200']])
@pytest.mark.parametrize('headers', [{'Content-Type': 'application/json', 'accept': 'application/json'}])
@pytest.mark.parametrize('data', [{
    "id": 0,
    "username": "User_name",
    "firstName": "f_User_name",
    "lastName": "l_User_name",
    "email": "User_name@gmail.com",
    "password": "qwerty",
    "phone": "1234567890",
    "userStatus": 0
}])
def test_create_new_user(api_post, api_request, data, headers):
    r = api_post
    print()
    # assert that http response == 200
    assert r['code'] == int(api_request[1])


# User login
@pytest.mark.parametrize('api_request', [['v2/user/login?username=User_name&password=qwerty', '200']])
@pytest.mark.parametrize('headers', [{'accept': 'application/json'}])
def test_user_login(api_get, api_request, headers):
    r = api_get
    # assert that http response == 200
    assert r == int(api_request[1])


# User logout
@pytest.mark.parametrize('api_request', [['v2/user/logout', '200']])
@pytest.mark.parametrize('headers', [{'accept': 'application/json'}])
def test_user_logout(api_get, api_request, headers):
    r = api_get
    # assert that http response == 200
    assert r == int(api_request[1])


# Update user
@pytest.mark.parametrize('api_request', [['v2/user/User_name', '200']])
@pytest.mark.parametrize('headers', [{'Content-Type': 'application/json', 'accept': 'application/json'}])
@pytest.mark.parametrize('data', [{
    "id": 0,
    "username": "User_name",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
}])
def test_update_user(api_put, api_request, data, headers):
    r = api_put
    print()
    # assert that http response == 200
    assert r['code'] == int(api_request[1])


# Get info about user
@pytest.mark.parametrize('api_request', [['v2/user/User_name', '200']])
@pytest.mark.parametrize('headers', [{'accept': 'application/json'}])
def test_user_logout(api_get, api_request, headers):
    r = api_get
    # assert that http response == 200
    assert r == int(api_request[1])


# User delete
@pytest.mark.trylast
@pytest.mark.parametrize('api_request', [['v2/user/User_name', '200']])
@pytest.mark.parametrize('headers', [{'accept': 'application/json'}])
def test_user_delete(api_get, api_request, headers):
    r = api_get
    # assert that http response == 200
    assert r == int(api_request[1])


# Add a new pet to the store
@pytest.mark.parametrize('api_request', [['v2/pet', 'doggie']])
@pytest.mark.parametrize('headers', [{'Content-Type': 'application/json', 'accept': 'application/json'}])
@pytest.mark.parametrize('data', [{
"id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}])
def test_add_new_pet(api_put, api_request, data, headers):
    r = api_put
    # assert that name is 'Doggie'
    assert r['name'] == api_request[1]


# Update existing pet
@pytest.mark.parametrize('api_request', [['v2/pet', 'Doggie_2']])
@pytest.mark.parametrize('headers', [{'Content-Type': 'application/json', 'accept': 'application/json'}])
@pytest.mark.parametrize('data', [{
"id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Doggie_2",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}])
def test_add_new_pet(api_put, api_request, data, headers):
    r = api_put
    # assert that name is 'Doggie_2'
    assert r['name'] == api_request[1]


# 1) get list of pets with status 'pending'
# 2) find pet with id 2
@pytest.mark.parametrize('api_request', [['v2/pet/findByStatus?status=pending', '200'], ['v2/pet/2', '200']])
@pytest.mark.parametrize('headers', [{'accept': 'application/json'}])
def test_user_logout(api_get, api_request, headers):
    r = api_get
    # assert that http response == 200
    assert r == int(api_request[1])

import pytest


# @pytest.mark.parametrize('api_request', [['api/users?page=2', '201'], ['api/users/2', '201'],
#                                          ['api/users/23', '404'], ['api/unknown', '200'],
#                                          ['https://reqres.in/api/unknown/2', '201'], ['api/unknown/23', '404']])
# def test_api_summation(api_client_get_status, api_request):
#     response = api_client_get_status
#     if response is True:
#         assert True


# @pytest.mark.parametrize('api_request', [['api/users?page=2', "data", '0', 'id', '7'],
#                                          ['api/users?page=2', "data", '0', 'email', 'michael.lawson@reqres.in'],
#                                          ['api/users?page=2', "data", '0', 'first_name', 'Michael'],
#                                          ['api/users?page=2', "data", '0', 'last_name', 'Lawson'],
#                                          ['api/users?page=2', "data", '0', 'avatar', 'https://reqres.in/img/faces/7-image.jpg'],
#                                          ['api/users?page=2', "data", '1', 'id', '8']
#                                          ])
# def test_api_summation(api_client_get_value, api_request):
#     api_response = api_client_get_value
#     try:
#         int(api_request[4])
#         assert api_response[api_request[1]][int(api_request[2])][api_request[3]] == int(api_request[4])
#     except ValueError:
#         assert api_response[api_request[1]][int(api_request[2])][api_request[3]] == api_request[4]


@pytest.mark.parametrize('api_request', ['api/users'])
@pytest.mark.parametrize('json_request', ['"name": "morpheus","job": "leader"'])
def test_api_post(api_client_post_value, api_request, json_request):
    api_response = api_client_post_value
    # print(api_response)











# response = requests.get('https://reqres.in/api/users?page=2')
# print('response.headers == ' + str(response.headers["Content-Type"]))  # application/json; charset=utf-8
# response_body = response.json()
# print('response_body["data"] == ' + str(response_body["data"][0]['id']))

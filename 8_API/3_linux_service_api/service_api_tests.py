import pytest


# Create strings for summation tests
# 1997, 3994, 5991, 7988, 9985, 11982, 13979, 15976, 17973, 998
number = []
for x in range(1, 3):
    if x < 10:
        append_number = str(x) * 1997
        number.append(append_number)
    else:
        append_number = str(10) * 998
        number.append(append_number)


# Testing that service return correct sum
@pytest.mark.parametrize('string_request', number)
def test_api_summation(api_client, string_request):
    response = api_client
    correct_result = int(string_request[0]) * 1997
    request_result = response.get('number')
    assert correct_result == request_result
    print("Correct result == " + str(correct_result) + ", Request result == " + str(request_result))


# roman numbers input
@pytest.mark.parametrize('string_request', ['XC_1'])
def test_api_roman_numbers(api_client, string_request):
    response = api_client
    request_result = response.get('number')
    assert response.get('number') == 1
    print(request_result)


# NOT ASCII input
@pytest.mark.parametrize('string_request', ['1あ-てる2'])
def test_api_not_ascii(api_client, string_request):
    response = api_client
    request_result = response.get('number')
    assert response.get('number') == 3
    print(request_result)


# only special character input
@pytest.mark.parametrize('string_request', ['!@#$%^&'])
def test_api_only_special_character_input(api_client, string_request):
    response = api_client
    request_result = response.get('number')
    assert response.get('number') == None
    print(request_result)


# boundary testing NULL input
@pytest.mark.parametrize('string_request', [''])
def test_api_boundary_testing_null_input(api_client, string_request):
    response = api_client
    request_result = response.get('number')
    assert response.get('number') == None
    print(request_result)


# boundary testing 1 char
@pytest.mark.parametrize('string_request', ['9'])
def test_api_boundary_testing_1_char(api_client, string_request):
    response = api_client
    request_result = response.get('number')
    assert response.get('number') == 9
    print(request_result)


# input 0
@pytest.mark.parametrize('string_request', ['0'])
def test_api_0_input(api_client, string_request):
    response = api_client
    request_result = response.get('number')
    assert response.get('number') == {}
    print(request_result)


# special characters, letters and numbers input
@pytest.mark.parametrize('string_request', ['19@9#9$9%9f9g9h9j9k9l9;9,9m9n9b9v9c9x9z9q9w9e1'])
def test_api_0_input(api_client, string_request):
    response = api_client
    request_result = response.get('number')
    assert response.get('number') == 200
    print(request_result)

# Mora than 1997 characters
@pytest.mark.xfail
@pytest.mark.parametrize('string_request', [str(1) * 1998])
def test_api_0_input(api_client, string_request):
    response = api_client
    request_result = response.get('number')
    assert response.get('number') == offset
    print(request_result)

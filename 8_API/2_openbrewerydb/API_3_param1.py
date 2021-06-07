import pytest
import requests

# def test_get_locations_for_us_90210_check_status_code_equals_200():
#     response = requests.get("https://api.openbrewerydb.org/breweries?by_city=san_diego")
#     print('response.status_code' + str(response.status_code))
#     assert response.status_code == 200

# def test_get_locations_for_us_90210_check_content_type_equals_json():
#     response = requests.get("https://api.openbrewerydb.org/breweries?by_city=san_diego")
#     print()
#     print('response.headers == ' + str(response.headers["Content-Type"]))
#     assert response.headers["Content-Type"] == "application/json; charset=utf-8"

# pytest API_3_param1.py --url=https://api.openbrewerydb.org/
@pytest.mark.parametrize('cityId', ['san_diego1', 'san_diego2'])
def test_api_filtering(api_client, cityId):
    res = api_client.get(
        path="/breweries",
        params={'by_city': cityId}
    )
    # this request return empty list
    assert res.json() == []


@pytest.mark.parametrize('cityId', ['san_diego', 'new_york'])
def test_api_filtering(api_client, cityId):
    res = api_client.get(
        path="/breweries",
        params={'by_city': cityId}
    )
    response = res.json()
    if cityId == 'new_york':
        city = 'New York'
    else:
        city = 'San Diego'
    print()
    print(city)

    assert response[0]['city'] == city

@pytest.mark.parametrize('stateId', ['Indiana', 'Oregon'])
def test_api_filtering(api_client, stateId):
    res = api_client.get(
        path="/breweries",
        params={'by_state': stateId}
    )
    response = res.json()
    if stateId == 'Indiana':
        state = 'Indiana'
    else:
        state = 'Oregon'
    print()
    print(state)

    assert response[1]['state'] == state
#
#
# https://api.openbrewerydb.org/breweries?per_page=25
@pytest.mark.parametrize('perPage', ['52', '20'])
def test_api_filtering(api_client, perPage):
    res = api_client.get(
        path="/breweries",
        params={'per_page': perPage}
    )
    response = res.json()
    print()
    print(len(response))
    print(perPage)
    if int(perPage) < 51:
        assert len(response) == int(perPage)
    else:
        assert len(response) == 50

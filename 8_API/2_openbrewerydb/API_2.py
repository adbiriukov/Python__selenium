import requests


def test_get_locations_for_us_90210_check_one_place_is_returned():
    response = requests.get("https://api.openbrewerydb.org/breweries")
    response_body = response.json()
    print(response_body)
    print(len(response_body))
    for x in range (0, 20):
        print()
        print(x)
        print(response_body[x]['id'])


    assert response_body[0]['country'] == "United States"
import requests


# def test_get_locations_for_us_90210_check_status_code_equals_200():
#     response = requests.get("http://api.zippopotam.us/us/90210")
#     print('response.status_code' + str(response.status_code))
#     assert response.status_code == 200


# def test_get_locations_for_us_90210_check_content_type_equals_json():
#     response = requests.get("http://api.zippopotam.us/us/90210")
#     print()
#     print('response.headers == ' + str(response.headers["Content-Type"]))
#     assert response.headers["Content-Type"] == "application/json"

def test_get_locations_for_us_90210_check_country_equals_united_states():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    print()
    print('response_body["country"] == ' + str(response_body["country"]))
    assert response_body["country"] == "United States"

# def test_get_locations_for_us_90210_check_city_equals_beverly_hills():
#     response = requests.get("http://api.zippopotam.us/us/90210")
#     response_body = response.json()
#     print('response_body["places"][0]["place name"] == ' + str(response_body["places"][0]["place name"]))
#     assert response_body["places"][0]["place name"] == "Beverly Hills"

def test_get_locations_for_us_90210_check_one_place_is_returned():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    print()
    print("len of places == " + str(len(response_body["places"])))
    assert len(response_body["places"]) == 1








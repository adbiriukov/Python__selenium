import requests

def test_answer(url_param):
    response = requests.get(url_param)
    assert response.status_code == 200

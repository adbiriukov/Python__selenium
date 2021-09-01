import pytest
import requests


@pytest.fixture()
def api_client(string_request):
    r = requests.post('http://127.0.0.1:8080/converter', json={"string": string_request})
    r = r.json()
    return r

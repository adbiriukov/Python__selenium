import pytest
import requests

# pytest API_3_param2.py --url=https://api.openbrewerydb.org/breweries?per_page=25
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
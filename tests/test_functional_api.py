from fastapi.testclient import TestClient
from beerlog.api import api


client = TestClient(api)


def test_create_beer_via_api():
    response = client.post(
        "/beers/",
        json={
            "name": "Skol",
            "style": "KornIPA",
            "flavor": 1,
            "image": 1,
            "cost": 2,
        },
    )
    #Checar pq no exemplo estava 201
    assert response.status_code == 200
    result = response.json()
    assert result["name"] == "Skol"
    assert result["id"] == 1



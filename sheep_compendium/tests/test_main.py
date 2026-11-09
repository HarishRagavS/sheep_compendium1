from typing import Dict

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200

    assert response.json() == {"id": 1, "name": "Spice", "breed":"Gotland", "sex":"ewe"}



def test_add_sheep():

    new_sheep = {"id": 7 , "name" : "Leo", "breed" : "F1", "sex": "ewe"}
    response = client.post("/sheep/", json=new_sheep)
    assert response.status_code == 201
    assert response.json() == new_sheep
    get_response = client.get("/sheep/7")
    assert get_response.status_code == 200
    assert get_response.json() == new_sheep


def test_read_all_sheep():
    response = client.get("/sheep/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 6

def test_update_sheep():
    update_sheep = {"id": 2, "name": "Jack", "breed": "Polypay", "sex": "ram"}
    response = client.put("/sheep/2", json=update_sheep)
    assert response.status_code == 200
    assert response.json() == update_sheep
    get_response = client.get("/sheep/2")
    assert get_response.status_code == 200
    assert get_response.json() == update_sheep

def test_delete_sheep():
    response = client.delete("/sheep/3")
    assert response.status_code == 204
    get_response = client.get("/sheep/3")
    assert get_response.status_code == 404
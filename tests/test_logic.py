from starlette.status import HTTP_200_OK
from starlite.testing import TestClient


def test_is_odd_true(test_client: TestClient):
    with test_client as client:
        response = client.get("/logic/isodd/3")
        assert response.status_code == HTTP_200_OK
        assert response.text == "true"


def test_is_odd_false(test_client: TestClient):
    with test_client as client:
        response = client.get("/logic/isodd/4")
        assert response.status_code == HTTP_200_OK
        assert response.text == "false"


def test_is_even_true(test_client: TestClient):
    with test_client as client:
        response = client.get("/logic/iseven/4")
        assert response.status_code == HTTP_200_OK
        assert response.text == "true"


def test_is_even_false(test_client: TestClient):
    with test_client as client:
        response = client.get("/logic/iseven/3")
        assert response.status_code == HTTP_200_OK
        assert response.text == "false"

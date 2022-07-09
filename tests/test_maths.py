from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from starlite.testing import TestClient


def test_add(test_client: TestClient):
    with test_client as client:
        response = client.get("/maths/add?first=1&second=2")
        assert response.status_code == HTTP_200_OK
        assert response.text == "3"


def test_subtract(test_client: TestClient):
    with test_client as client:
        response = client.get("/maths/subtract?first=7&second=2")
        assert response.status_code == HTTP_200_OK
        assert response.text == "5"


def test_multiply(test_client: TestClient):
    with test_client as client:
        response = client.get("/maths/multiply?first=5&second=4")
        assert response.status_code == HTTP_200_OK
        assert response.text == "20"


def test_divide(test_client: TestClient):
    with test_client as client:
        response = client.get("/maths/divide?first=20&second=5")
        assert response.status_code == HTTP_200_OK
        assert response.text == "4.0"


def test_divide_by_zero(test_client: TestClient):
    with test_client as client:
        response = client.get("/maths/divide?fist=10&second=0")
        assert response.status_code == HTTP_400_BAD_REQUEST

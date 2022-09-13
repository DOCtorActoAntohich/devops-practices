from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from app_python.main import app as app_root

client = TestClient(app_root)


def test_root_page():
    timezone = "Europe/Moscow"

    response = client.get("/")
    assert response.status_code == HTTP_200_OK

    response_text = response.json()
    assert response_text.startswith(f"Current time in {timezone} is:")


def test_existing_timezone():
    timezone = "America/New_York"

    response = client.get(f"/{timezone}")
    assert response.status_code == HTTP_200_OK

    response_text = response.json()
    assert response_text.startswith(f"Current time in {timezone} is:")


def test_non_existent_timezone():
    timezone = "Amogus/Sus"

    response = client.get(f"/{timezone}")
    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.json() == {
        "error_details": f"Invalid IANA time zone name: {timezone}"
    }

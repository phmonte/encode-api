from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_encode_with_zero():
    response = client.get("/encode/00003039")
    assert response.status_code == 200
    assert response.json() == '00000bdf'


def test_encode_ok():
    response = client.get("/encode/12345678")
    assert response.status_code == 200
    assert response.json() == '00bc614e'


def test_encode_with_numbers_greater_than_8_characters():
    response = client.get("/encode/1234567878787")
    assert response.status_code == 400
    assert response.json() == {'detail': 'The number cannot be greater than 99999999', 'headers': None,
                               'status_code': 400}


def test_encode_with_1_character():
    response = client.get("/encode/5")
    assert response.status_code == 200
    assert len(response.json()) == 8


def test_decode_ok():
    response = client.get("/decode/bc614e")
    assert response.status_code == 200
    assert response.json() == 12345678


def test_decode_with_invalid_string_decode():
    response = client.get("/decode/g")
    assert response.status_code == 500
    assert response.json() == {'detail': 'An error occurred while decoding', 'headers': None, 'status_code': 500}

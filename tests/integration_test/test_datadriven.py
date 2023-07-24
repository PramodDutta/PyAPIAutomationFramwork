import pytest
import requests
import json


@pytest.fixture
def test_data():
    with open('test_data.json') as f:
        data = json.load(f)
    return data

#
# test_data = [
#     {'username': 'admin', 'password': 'password123'},
#     {'username': 'user2', 'password': 'pw2'}
# ]


@pytest.mark.parametrize("row", test_data)
def test_login(row):
    url = 'https://restful-booker.herokuapp.com/auth'
    resp = requests.post(url, json={
        'username': row['username'],
        'password': row['password']
    })
    assert resp.status_code == 200
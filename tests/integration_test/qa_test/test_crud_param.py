import json
import os

import pytest
import requests
from dotenv import load_dotenv


@pytest.fixture
def json_data():
    with open('tests/pytestDemo/readfromjson/stage_data.json', 'r') as f:
        data = json.load(f)
    return data


def test_get_req(json_data):
    response = requests.get(json_data["url"])
    print(json_data["url"])
    # print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_post_req():
    load_dotenv()
    username = os.getenv("username")
    password = os.getenv("password")
    print(username, password)

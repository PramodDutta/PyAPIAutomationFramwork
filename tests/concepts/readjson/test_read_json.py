import json
import pytest
import json
import pytest
from dotenv import  load_dotenv
import os
@pytest.fixture
def load_json_data():
    load_dotenv()
    file_name = os.getenv("load_env")
    print(file_name)
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data


def test_make_req(load_json_data):
    print(load_json_data["url"])

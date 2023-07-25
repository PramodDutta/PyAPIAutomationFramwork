import openpyxl
import requests


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})

    return credentials


def make_auth_request(username, password):
    payload = {
        "username": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post("https://restful-booker.herokuapp.com/auth", headers=headers, json=payload)
    # tO verify that Expected Result == Actual Result
    assert response.status_code == 200
    print(response.text)
    print(response.json()["token"])
    return response


def test_post_create_token():
    file_path = "testdata_ddt.xlsx"
    credentials = read_credentials_from_excel(file_path)

    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)

        response = make_auth_request(username, password)

        assert response.status_code == 200

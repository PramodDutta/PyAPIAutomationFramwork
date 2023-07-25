import os

import dotenv
from dotenv import load_dotenv
import requests
import pytest

@pytest.fixture
def test_post_create_booking():
    payload_create_booking = {
        "firstname": "Pramod",
        "lastname": "Dutta",
        "totalprice": 10000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2022-12-28",
            "checkout": "2023-01-02"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {
        "Content-Type": "application/json",
    }
    # Additonal Information that we need to send the to Server to let server know that we are
    # sending a json payload in the request

    response = requests.post("https://restful-booker.herokuapp.com/booking", headers=headers,
                             json=payload_create_booking)
    print(response.json())
    booking_id = response.json()["bookingid"]
    print(booking_id)
    print(response.headers)
    assert response.status_code == 200
    return booking_id

    # More Assert - More No of Testcases - More No Assertion
    # Passing the data between the Testcases


#
#
def test_put_req(test_post_create_booking):
    payload_create_booking = {
        "firstname": "Amit",
        "lastname": "Singh",
        "totalprice": 1337,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-12-28",
            "checkout": "2024-01-02"
        },
        "additionalneeds": "Breakfast,Lunch"
    }
    load_dotenv()
    temp_token = "token=" + os.getenv("token")
    print(temp_token)
    print(os.getenv("username"))
    headers = {
        "Content-Type": "application/json",
        "Cookie": temp_token
    }
    url_put = "https://restful-booker.herokuapp.com/booking/" + str(test_post_create_booking)
    response = requests.put(url_put, headers=headers,
                            json=payload_create_booking)
    print(response.text)
    print(response.status_code)
    assert response.status_code == 200


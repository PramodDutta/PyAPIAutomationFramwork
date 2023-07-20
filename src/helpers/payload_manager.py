def payload_create_booking():
    # In future you can replace this from the excel or JSON
    payload = {
        "firstname": "Pramod",
        "lastname": "Dutta",
        "totalprice": 432,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2022-01-01",
            "checkout": "2022-01-01"
        },
        "additionalneeds": "Lunch"
    }
    return payload


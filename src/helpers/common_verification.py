# HTTP Status Code
def verify_http_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Expected HTTP Status : " + expected_data


# Any key, should not be null, of empty
def verify_key_for_not_null_greater_than_zero(key):
    assert key != 0, "Key is non Empty : " + key
    assert key > 0, "Key should be greater than zero : " + key

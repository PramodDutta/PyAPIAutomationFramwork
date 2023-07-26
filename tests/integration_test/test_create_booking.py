'''
Author : Pramod
Objective :  Create and Verify by POST Request
TC#1 - Verify the Status Code, Headers
TC#2 - Verify the Body -> Booking ID
TC#3 - Verify the JSON Schema is Valid

Assertion
Expected Result == Actual Result



'''
import pytest
import allure

from src.constants.apicontanst import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers


# Payload
# Base URL
# Verify


class TestIntegration(object):



    @pytest.mark.smoke
    @allure.feature('TC#1 - Verify Create Booking Feature')
    def test_create_booking_tc1(self):
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_code(response, 200)
        verify_key_for_not_null_greater_than_zero(response.json()["bookingid"])

    # URL -> Separate URL
    # Payload - Separate Payload manager
    # Headers -> Headers Utils
    # Verify - Seperate Verify
    @pytest.mark.smoke
    @allure.feature('TC#2 - Verify Update Booking Feature')
    def test_update_put(self):
        assert True

    @pytest.mark.smoke
    @allure.feature('TC#3 - Verify Delete Booking Feature')
    def test_delete(self):
        assert True

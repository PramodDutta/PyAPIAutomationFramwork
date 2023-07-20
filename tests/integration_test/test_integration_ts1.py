'''
Author : Pramod
Objective :  # Verify that Creating a Booking and Updating it and Delete it

Assertion
Expected Result == Actual Result



'''

from src.constants.apicontanst import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers


# Payload
# Base URL
# Verify


class TestIntegrationTC1(object):

    # URL -> Separate URL
    # Payload - Separate Payload manager
    # Headers -> Headers Utils
    # Verify - Seperate Verify

    def test_verify_creating_booking_by_updating_deleting(self):
        pass



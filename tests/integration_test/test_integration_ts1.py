'''
Author : Pramod
Objective :  # Verify that Creating a Booking and Updating it and Delete it

Assertion
Expected Result == Actual Result



'''

import pytest
# Payload
# Base URL
# Verify
@pytest.fixture()
def resource(request):
    print("setup")

    def teardown():
        print("teardown")

    request.addfinalizer(teardown)

    return "resource"


class TestIntegrationTC1(object):

    # URL -> Separate URL
    # Payload - Separate Payload manager
    # Headers -> Headers Utils
    # Verify - Seperate Verify

    def test_verify_creating_booking_by_updating_deleting(self):
        pass

# Add your contants here

# Adding my URL constants. Python -> functions

def base_url():
    # Change based on the env.json - Stage, preprod, Prod
    # In future I will write a login to change the base url based on the env
    return "https://restful-booker.herokuapp.com"


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


# qa.json
# url - https://qa-restful-booker.herokuapp.com/booking
# stage - https://stage-booker.herokuapp.com/booking
# prod - https://restful-booker.herokuapp.com/booking


# .env-qa
# # qa - https://qa-restful-booker.herokuapp.com/booking
# .env-stage
# # stage - https://stage-booker.herokuapp.com/booking
# ..env-prod
# # prod - https://restful-booker.herokuapp.com/booking



def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


def url_update_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + booking_id

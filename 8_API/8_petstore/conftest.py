import requests
import pytest
from random import choice


@pytest.fixture()
def api_get_pet(api_request, headers):
    # r = requests.get("https://"+str(login_pass)+"@restful-booker.herokuapp.com/"+str(api_request[0])+"")
    r = requests.get("https://petstore.swagger.io/"+str(api_request[0])+"", headers)
    r = r.status_code
    return r



@pytest.fixture()
def api_post_order(api_request, data, headers):
    r = requests.post("https://petstore.swagger.io/"+str(api_request[0])+"", json=data, headers=headers)
    r = r.json()
    return r
#
#
# # # To post
# @pytest.fixture()
# def api_client_post(generate_booking):
#     r = requests.post("https://restful-booker.herokuapp.com/booking/", json=generate_booking)
#     print(generate_booking)
#     r = r.status_code
#     return r
#
#
# # Update booking
# @pytest.fixture()
# def api_client_put(get_authtoken, generate_booking, firstname='Jim', lastname='Brown', totalprice=111, depositpaid=True,
#                    checkin='2018-01-01', additionalneeds='Breakfast'):
#     r = requests.post("https://restful-booker.herokuapp.com/booking/", json=generate_booking)
#     booking_id = r.json()['bookingid']
#     r = requests.put('https://restful-booker.herokuapp.com/booking/{:d}/'.format(booking_id), json={
#         "firstname": firstname,
#         "lastname": lastname,
#         "totalprice": totalprice,
#         "depositpaid": depositpaid,
#         "bookingdates": {
#             "checkin": checkin,
#             "checkout": checkin
#         },
#         "additionalneeds": additionalneeds
#     }, cookies={
#         "token": get_authtoken
#     })
#     return r.json()
#
#
# @pytest.fixture()
# def remove_booking(generate_booking, get_authtoken):
#     # Generate new booking to get id
#     r = requests.post("https://restful-booker.herokuapp.com/booking/", json=generate_booking)
#     booking_id = r.json()['bookingid']
#     # Remove booking
#     return requests.delete('https://restful-booker.herokuapp.com/booking/{:d}/'.format(booking_id), cookies={
#         "token": get_authtoken
#     })
#
#
# @pytest.fixture()
# def get_authtoken(username='admin', password='password123'):
#     url = "https://restful-booker.herokuapp.com/auth"
#     return requests.post(url, json={
#         "username": username,
#         "password": password
#     }).json()['token']
#
#
# # Generate new booking
# @pytest.fixture()
# def generate_booking():
#     firstname = choice(['Bart', 'Maggie', 'Lisa', 'Marge', 'Homer'])
#     lastname = choice(['Simpson', 'Smithers', 'Burns', 'Krustofsky'])
#     totalprice = choice([112, 113, 114, 115, 116, 117, 300, 999])
#     depositpaid = choice([True, False])
#     checkin = choice(['2018-02-02', '2018-03-03', '2018-04-04', '2018-05-05', '2018-06-11'])
#     checkout = choice(['2018-02-7', '2018-03-08', '2018-04-09', '2018-05-10', '2018-06-21'])
#     additionalneeds = choice(['Breakfast', 'Mini Fridge', 'Extra towel', 'Dinner'])
#
#     return (
#         {
#             "firstname": firstname,
#             "lastname": lastname,
#             "totalprice": totalprice,
#             "depositpaid": depositpaid,
#             "bookingdates": {
#                 "checkin": checkin,
#                 "checkout": checkout
#             },
#             "additionalneeds": additionalneeds
#         }
#     )

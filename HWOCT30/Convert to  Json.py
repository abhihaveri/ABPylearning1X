'''Program 5:
Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data'''

Booking_Details={
"bookingid": 2384,
"booking": {
"firstname": "PRAMOD",
"lastname": "Dutta",
"totalprice": 432,
"depositpaid": False,
"bookingdates": {
"checkin": "2022-01-01",
"checkout": "2022-01-01"
},
"additionalneeds": "Lunch"
}
}
#print(type(Booking_Details))
print(f'The Booking Id is {Booking_Details["bookingid"]}')
print(f'The Booking Dates are as Below:-\n{Booking_Details["booking"]["bookingdates"]}')
#first u should install phonenumbers library through -- pip install phonenumbers

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

number = input("Enter the number: ")
phone_numbers = phonenumbers.parse(number)

print(f"Location: {geocoder.description_for_number(phone_numbers, 'en')}")

print(f"Carrier: {carrier.name_for_number(phone_numbers, 'en')}")

print(f"Time Zone: {timezone.time_zones_for_number(phone_numbers,)}")

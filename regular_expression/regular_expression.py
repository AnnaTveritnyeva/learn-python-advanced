import re

pattern = (r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")
c = re.compile(pattern)


def check_phone_number():
    phone_number = input("phone number:")
    if c.search(phone_number):
        return "OK"
    return "WRONG"


print(check_phone_number())

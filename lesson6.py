try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(f"u cant divide by zero! {e}")
finally:
    print("smth")
try:
    number = int(input("Enter num:"))
except ValueError as e:
    print(e)


text = input("Enter text")
if type(text) != str:
    raise TypeError(f"We cant work with {type(text)} type")


class BuildingError(Exception):
    def __str__(self):
        return "Not enought materials"

def check_materials(amont_materials, limit_materials):
    if amont_materials > limit_materials:
        print("Enought materials!")
    else:
        raise(BuildingError)

my_materials = 400
check_materials(my_materials, 300)

class InvalidEmailError(Exception):
    def __init__(self, email):
        self.email = email

def send_email(email, message):
    if "@" not in email:
        raise InvalidEmailError("Invalid Email" + email)

try:
    send_email("example_email.com", "Hello!")
except InvalidEmailError as e:
    print(e)


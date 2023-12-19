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
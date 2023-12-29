def calculator(expression, precision=2):
    try:
        result = eval(expression)
        rounded_result = round(result, precision)
        return rounded_result
    except Exception as e:
        print(f"Error: {e}")
        return None

def calculate(expression):
    return calculator(expression)

result = calculate("2 + 2")
print(result)

result = calculate("10 / 0")
print(result)
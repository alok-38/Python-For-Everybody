def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(a, b):
    sum_result = add(a, b)
    sub_result = subtract(a, b)
    mul_result = multiply(a, b)
    div_result = divide(a, b)
    return sum_result, sub_result, mul_result, div_result

print(calculate(5, 2))

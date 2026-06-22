def calculate_sum(integers):
    total = 0
    for value in integers:
        total += value
    return total

def calculate_average(integers):
    return calculate_sum(integers) / len(integers)

print(calculate_average([1, 2, 3, 4, 5]))
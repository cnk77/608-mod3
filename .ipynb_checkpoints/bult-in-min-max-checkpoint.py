# Module 3 File 1 - building a maximum and minimum function

# Kyle Hudson

def maximum(value1, value2, value3):
    """Return the maximum value of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

def minimum(value1, value2, value3):
    "Return the minimum value of three values."""
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    return min_value

value1 = int(input('Value 1:'))
value2 = int(input('Value 2:'))
value3 = int(input('Value 3:'))

print('Maximum value =', maximum(value1, value2, value3))
print('Minimum value =', minimum(value1, value2, value3))
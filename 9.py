def multiply(a, b):
    result = a * b
    result2 = a ** b
    return result, result2


c = multiply(5, 6)
print(type(c))
print(c[0])
print(c[1])
multiply(2, 3)
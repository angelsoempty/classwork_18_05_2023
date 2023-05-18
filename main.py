#4
def multiply_by(n):
    def multiply(x):
        return x * n
    return multiply
multiply_by_5 = multiply_by(5)
result = multiply_by_5(10)
print(result)

multiply_by_3 = multiply_by(3)
result = multiply_by_3(7)
print(result)
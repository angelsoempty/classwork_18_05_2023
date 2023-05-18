#2
class SquareGenerator:
    def __init__(self, n):
        if not isinstance(n, (int, float)):
            raise TypeError('це повинно бути числом')
        self.n = n
    def generator_square(self):
        for i in range(1, int(self.n) + 1):
            yield i ** 2
#приклад використання
try:
    for num in SquareGenerator(20).generator_square():
        print(num)
except TypeError as e:
    print(e)
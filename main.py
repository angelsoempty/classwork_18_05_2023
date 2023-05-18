#3
class ListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.current_index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_index >= len(self.lst):
            raise StopIteration
        else:
            result = self.lst[self.current_index]
            self.current_index += 1
            return result

numbers = [1, 2, 3, 4, 5]
iterator = ListIterator(numbers)

for num in iterator:
    print(num)
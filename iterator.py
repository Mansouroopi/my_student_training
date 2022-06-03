# implementation of for loop in python
iterable = [1, 2, 3, 4]
iter_obj = iter(iterable)
while True:
    try:
        element = next(iter_obj)
        # do something the elements
        # print(element)
    except StopIteration:
        break

class PowerTwo:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self.n

    def __next__(self):
        if self.n <=self.max:
            result = 2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration

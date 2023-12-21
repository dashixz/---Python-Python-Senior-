
lst = ["one", 2, 3]
index = lst[0]
print(index)
# for elem in lst:
#     print(elem)
iterator = iter(lst)
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
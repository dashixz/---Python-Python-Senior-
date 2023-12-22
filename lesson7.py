#iterator
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

my_list = [1, 6, 3, 9, 5]
my_iterator = MyIterator(my_list)
print(my_iterator.__iter__())
print(*my_iterator)

#generator
def my_generator(data):
    for item in data:
        yield item

my_list = [1, 6, 3, 9, 5]
my_gen = my_generator(my_list)
print(*my_gen)

#closure
def outer_function():
    x = 10
    def inner_function(y):
        return  x + y
    return inner_function
closure = outer_function()
print(closure(15))
print(closure(100))
print(closure(5))

#decorator
def my_decorator(func):
    def wrapper():
        print("Starting wpapping")
        func()
        print("Ending wrapping")
    return wrapper
@my_decorator
def my_func():
    print("Hello!")

#say_hello = my_decorator(my_func)
#say_hello()
my_func()
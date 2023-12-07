class Grandparent:
    height = 170
    eyes = "light blue"
    age = 70
class Parent(Grandparent):
    age = 40
class Child(Parent):
    height = 165
    age = 15
    def __init__(self):
        print(self.height)
        print(self.eyes)
        print(self.age)

eric = Child()
class Human:
    height = 170
class Student(Human):
    pass
class Worker(Human):
    pass
nick = Student()
kate = Worker()
print(nick.height, kate.height)



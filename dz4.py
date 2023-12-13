class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Generic animal sound"

    def sleep(self):
        return f"{self.name} is sleeping"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

    def chase_laser(self):
        return f"{self.name} is chasing the laser pointer"

class Bunny(Animal):
    def make_sound(self):
        return "Nom nom nom (eating sound)"

    def hop(self):
        return f"{self.name} is hopping around"

# Simulation
dog_name = "Snow"
cat_name = "Fluffy"
bunny_name = "Silver"

dog = Dog(name=dog_name)
cat = Cat(name=cat_name)
bunny = Bunny(name=bunny_name)

print(f"{dog.name} says: {dog.make_sound()}")
print(f"{cat.name} says: {cat.make_sound()}")
print(f"{bunny.name} says: {bunny.make_sound()}")

print(dog.fetch())
print(cat.chase_laser())
print(bunny.hop())

print(dog.sleep())
print(cat.sleep())
print(bunny.sleep())
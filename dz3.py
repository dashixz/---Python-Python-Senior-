class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def main():
    dog_name = "Goldie"
    cat_name = "Sammy"

    dog = Dog(name=dog_name)
    cat = Cat(name=cat_name)

    print(f"{dog.name} says: {dog.make_sound()}")
    print(f"{cat.name} says: {cat.make_sound()}")

if __name__ == "__main__":
    main()

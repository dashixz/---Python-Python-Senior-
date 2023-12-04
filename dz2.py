class cats_life:
    def __init__(self, name, gen, age, characteristics, breed):
        self.name = name
        self.gen = gen
        self.characteristics = characteristics
        self.age = age
        self.age +=1
        self.breed = breed
cat1 = cats_life("Fluffy", "girl", 1, "A rugged-looking coat designed for cold Scandinavian winters, almond-shaped eyes, calm demeanor", "Norwegian Forest Cat")
cat1 = cats_life("", "boy", 2, "Round head, small ears, big eyes and a long, luxurious coat; they are quiet and easy-going", "Persian")
cat1 = cats_life("", "", 1, "", "")
cat1 = cats_life("", "", 1, "", "")
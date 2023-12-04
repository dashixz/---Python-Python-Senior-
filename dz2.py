class cats_life:
    def __init__(self, name, gen, age, characteristics, breed):
        self.name = name
        self.gen = gen
        self.characteristics = characteristics
        self.age = age
        self.age +=1
        self.breed = breed
cat1 = cats_life("Fluffy", "girl", 1, "A rugged-looking coat designed for cold Scandinavian winters, almond-shaped eyes, calm demeanor", "Norwegian Forest Cat")
cat2 = cats_life("Snowflake", "girl", 2, "Round head, small ears, big eyes and a long, luxurious coat; they are quiet and easy-going", "Persian")
cat3 = cats_life("Moonlight", "boy", 0, "Blue eyes with long, light-colored coats. Easy disposition, gentle and friendly with animals and humans. ", "Ragdoll")
cat4 = cats_life("Shadow", "boy", 6, "Intelligent, kind, and companionable, with about 75 different color combinations ", "Maine Coon Cat")
print("Our first cat breed is -", cat1.name)
print("Fourth cat have some interesting characteristics -", cat4.characteristics)
print("Btw second cat have a really cute name -", cat2.characteristics)
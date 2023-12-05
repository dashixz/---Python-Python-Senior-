
import random
class Human:
    def __init__(self,
                 name = "Human",
                 job = None,
                 home = None,
                 car = None):
        self.name = name
        self.money = 50_000
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        pass

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def shoping(self):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
    def days_indexes(self, day):
        pass
    def is_alive(self):
        pass
    def live(self, day):
        pass

class Auto:
    def __init__(self, band_list):
        self.brand = random.choice(list(band_list))
        self.fuel = band_list[self.brand]["fuel"]
        self.strength = band_list[self.brand]["strength"]
        self.consumption = band_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 0.5
            return True
        else:
            print("Car cant move")
            return False


brands_of_car = {
            "BMW": {"fuel": 120, "strength":720, "consumption": 17},
            "McLaren": {"fuel": 80, "strength": 800, "consumption": 4},
            "Lamborghini": {"fuel": 90, "strength": 780, "consumption": 17},
            "Porsche": {"fuel": 110, "strenght": 330, "consumption": 11}
        }
nick = Human(name = "Max")
nick.get_car()
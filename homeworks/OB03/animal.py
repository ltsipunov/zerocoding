from random import random

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 70
        self.loss = 5
        self.disease = 0

    def temperature(self):
        return round(36.9 + self.disease / 10, 1)

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")
    def weight(self):
        if not self.max_weight:
            raise NotImplementedError("Subclass or instance must implement property max_weight")
        return round(self.max_weight*(100-self.health/2)/100,2)

    def eat(self):
        self.health+=10
        print( f"{self.name} поел. Вес {self.weight()}" )

    def recover(self):
        self.disease = max( self.disease-10, 0)
        if self.disease>0:
            print( f"{self.name} выздоравливает . Температура {self.temperature()}" )
        else:
            print( f"{self.name} здоров . {self.make_sound()}" )

    def day(self):
        d = int( (random() * 100 - 80))
        self.disease +=  d if d>0 else 0
        self.health -= self.loss + self.disease
        if self.disease> 0: print(f" {self.name} болен. Температура {self.temperature()}  ")

    def is_alive(self):
        if self.health > 100:
            print(f"{self.name}  ЛОПНУЛ! от переедания ")
            return False
        if self.health < 0:
            print(f"{self.name}  умер от болезней и тоски  :( ")
            return False
        return True

class Bird(Animal):
    max_weight=5
    def make_sound(self):
        return f"{self.name} says: Чик-чирик!"

class Mammal(Animal):
    max_weight=50
    def make_sound(self):
        return f"{self.name} says: Фрх-ру!"

class Reptile(Animal):
    max_weight=20
    def make_sound(self):
        return f"{self.name} says:  шшшшш!"

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())
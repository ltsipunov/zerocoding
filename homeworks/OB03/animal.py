class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def eat(self):
        return f"{self.name} is eating."


class Bird(Animal):
    def make_sound(self):
        return f"{self.name} says: Чик-чирик!"


class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} says: Фрх-ру!"


class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} says:  шшшшш!"


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())
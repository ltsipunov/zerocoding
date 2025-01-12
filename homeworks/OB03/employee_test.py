from animal import *
from employee import *

parrot = Bird("Parrot", 2)
lion = Mammal("Lion", 5)
snake = Reptile("Snake", 3)

keeper = ZooKeeper("Alice")
vet = Veterinarian("Bob")

animals = [parrot, lion, snake]

for animal in animals:
    print(keeper.perform_duties(animal))
    print(vet.perform_duties(animal))
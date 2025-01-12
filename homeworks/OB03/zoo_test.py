from zoo import *
from animal import *
from employee import *

zoo = Zoo("Wildlife Zoo")

parrot = Bird("Parrot", 2)
lion = Mammal("Lion", 5)
snake = Reptile("Snake", 3)

keeper = ZooKeeper("Alice")
vet = Veterinarian("Bob")

zoo.add_animal(parrot)
zoo.add_animal(lion)
zoo.add_animal(snake)

zoo.add_employee(keeper)
zoo.add_employee(vet)

zoo.assign_animal_to_employee(keeper, parrot)
zoo.assign_animal_to_employee(vet, lion)
zoo.assign_animal_to_employee(keeper, snake)
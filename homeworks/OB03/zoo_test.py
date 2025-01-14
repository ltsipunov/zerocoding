from zoo import *
from animal import *
from employee import *
# In this test I left one loose animal and one with two keepers, so I expect these ones must die of hunger or overeating
# Destiny of other animals depends on their luck

zoo = Zoo("Wildlife Zoo")

parrot = Bird("Попугай", 2)
kiwi = Bird("Киви", 3)
lion = Mammal("Лев", 5)
giraffe = Mammal("Жираф", 8)
otter = Mammal("Ондатра", 5)
snake = Reptile("Питон", 3)

keeper = ZooKeeper("Alice")
vet = Veterinarian("Bob")
keeper_jr = ZooKeeper("Charlie")
zoo.add_employee(keeper)
zoo.add_employee(vet)
zoo.add_employee(keeper_jr)

zoo.add_animal(parrot)
zoo.add_animal(kiwi)
zoo.add_animal(giraffe)
zoo.add_animal(otter)
zoo.add_animal(lion)
zoo.add_animal(snake)

zoo.assign_animal_to_employee(keeper, parrot)
zoo.assign_animal_to_employee(keeper, snake)
zoo.assign_animal_to_employee(keeper, kiwi)
zoo.assign_animal_to_employee(keeper_jr, lion)
zoo.assign_animal_to_employee(keeper_jr, snake)
zoo.assign_animal_to_employee(keeper_jr, giraffe)

zoo.assign_animal_to_employee(vet, lion)
zoo.assign_animal_to_employee(vet, snake)
zoo.assign_animal_to_employee(vet, kiwi)
zoo.assign_animal_to_employee(vet, giraffe)

for i in range(20):
    print(f"======= День {i} =========")
    zoo.day()
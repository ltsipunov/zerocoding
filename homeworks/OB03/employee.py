class ZooEmployee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.animals=[]

    def perform_duties(self, animal):
        raise NotImplementedError("Subclass must implement abstract method")

    def add(self,animal):
        self.animals += [animal]

    def remove(self,animal):
        if animal in self.animals:
            self.animals.remove(animal)

    def day(self):
        for a in self.animals:
            self.perform_duties(a)

class ZooKeeper(ZooEmployee):
    def __init__(self, name):
        super().__init__(name, "Zoo Keeper")

    def perform_duties(self, animal):
        print(f"{self.name} is feeding {animal.name}.")
        animal.eat()

class Veterinarian(ZooEmployee):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def perform_duties(self, animal):
       if animal.disease > 0 :
            print (f"{self.name} лечит {animal.name}.")
            animal.recover()
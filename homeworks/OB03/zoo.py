class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to the zoo.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} has been added as a {employee.position}.")

    def assign_animal_to_employee(self, employee, animal):
        if animal in self.animals and employee in self.employees:
            employee.add(animal)
            print(f"{employee.name} is now responsible for {animal.name}.")
        else:
            print("Employee or animal not found in the zoo.")

    def remove(self,animal):
        for e in self.employees:
            e.remove(animal)
        self.animals.remove(animal)

    def day(self):
        for e in self.employees:
            e.day()
        for a in self.animals:
            a.day()
            if not a.is_alive():
                print(f"{a.name} помер :(  Исключаем {a.name} из списков....")
                self.remove(a)
        if not self.animals:
            print('В общем, все умерли :(....  Зоопарк закрывается')
            exit(0)
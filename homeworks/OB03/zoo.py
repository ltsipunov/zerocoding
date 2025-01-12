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
            print(f"{employee.name} is now responsible for {animal.name}.")
        else:
            print("Employee or animal not found in the zoo.")
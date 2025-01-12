class ZooEmployee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def perform_duties(self, animal):
        raise NotImplementedError("Subclass must implement abstract method")


class ZooKeeper(ZooEmployee):
    def __init__(self, name):
        super().__init__(name, "Zoo Keeper")

    def perform_duties(self, animal):
        return f"{self.name} is feeding {animal.name}."


class Veterinarian(ZooEmployee):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def perform_duties(self, animal):
        return f"{self.name} is treating {animal.name}."
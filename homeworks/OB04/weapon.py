from abc import ABC, abstractmethod
import random

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def explain(self,damage):
        pass


# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        damage = random.randint(15, 30)  # Урон меча
        return damage

    def explain(self, damage):
        return f"бьёт мечом и наносит {damage} урона!"

class Bow(Weapon):
    def attack(self):
        damage = random.randint(10, 25)  # Урон лука
        return damage

    def explain(self,damage):
        return f"стреляет из лука и наносит {damage} урона!"
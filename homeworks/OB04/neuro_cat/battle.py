from abc import ABC, abstractmethod
import random

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        damage = random.randint(15, 30)  # Урон меча
        print(f"Вы используете меч и наносите {damage} урона!")
        return damage


class Bow(Weapon):
    def attack(self):
        damage = random.randint(10, 25)  # Урон лука
        print(f"Вы используете лук и наносите {damage} урона!")
        return damage


# Класс Fighter
class Fighter:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f"{self.name} сменил оружие на {self.weapon.__class__.__name__}.")

    def attack(self, monster):
        damage = self.weapon.attack()
        monster.take_damage(damage)

    def is_alive(self):
        return self.health > 0


# Класс Monster
class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил {damage} урона! Осталось здоровья: {self.health}")

    def is_alive(self):
        return self.health > 0


# Функция для демонстрации боя
def battle(fighter, monster):
    print(f"Бой начался между {fighter.name} и {monster.name}!\n")
    while fighter.is_alive() and monster.is_alive():
        fighter.attack(monster)
        if monster.is_alive():
            damage = random.randint(5, 15)  # Урон от монстра
            fighter.health -= damage
            print(f"{monster.name} атакует {fighter.name} и наносит {damage} урона! Осталось здоровья: {fighter.health}\n")
        else:
            print(f"{monster.name} повержен! {fighter.name} победил!\n")
            break

    if not fighter.is_alive():
        print(f"{fighter.name} повержен! {monster.name} победил!\n")


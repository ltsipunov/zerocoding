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

class Actor(ABC):
    @abstractmethod
    def is_alive(self):
        pass

    @abstractmethod
    def relax(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def take_damage(self):
        pass

# Класс Fighter
class Fighter(Actor) :
    def __init__(self, name, weapon):
        self.name = name
        self.health  =100
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f"{self.name} сменил оружие на {self.weapon.__class__.__name__}.")

    def attack(self, monster):
        damage = self.weapon.attack()
        print(f"{self.name} "+self.weapon.explain(damage) )
        monster.take_damage(damage)

    def take_damage(self,damage):
        print(f"{self.name} получил {damage} урона! Осталось здоровья: {self.health}")
        self.health = max(0,self.health - damage)

    def relax(self):
        self.health = ( self.health+100 )//2
        print(f"{self.name} подкрепилсяю Сила выросла до {self.health}  ")

    def is_alive(self):
        return self.health > 0

# Класс Monster
class Monster(Actor):
    def __init__(self, name):
        self.name = name
        self.health=100

    def take_damage(self, damage):
        self.health = max(0,self.health - damage)
        print(f"{self.name} получил {damage} урона! Осталось здоровья: {self.health}")

    def attack(self,enemy):
        damage = random.randint(5, 15)  # Урон от монстра
        enemy.take_damage(damage)

    def is_alive(self):
        return self.health > 0

    def relax(self):
        self.health = ( 3*self.health+100 )//4
        print( f"{self.name} зализывает раны. Силы выросли  {self.health} " )

# Функция для демонстрации боя
def battle(fighter, monster):
    print(f"Бой начался между {fighter.name} и {monster.name}!\n")
    while fighter.is_alive() and monster.is_alive():
        fighter.attack(monster)
        if monster.is_alive():
            monster.attack(fighter)
            print(f"{monster.name} кусает {fighter.name} ! Осталось здоровья: {fighter.health}\n")
        else:
            print(f"{monster.name} повержен! {fighter.name} победил!\n")
            break

    if not fighter.is_alive():
        print(f"{fighter.name} повержен! {monster.name} победил!\n")

# Восстановление сил для следующего боя
def time_out(fighter, monster):
    print("Истощенные противники восстанавливают силы")
    for x in [ fighter,monster] : x.relax()

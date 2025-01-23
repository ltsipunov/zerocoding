from abc import ABC, abstractmethod
from weapon import *
import random

class Actor(ABC):
    def __init__(self, name):
        self.name = name
        self.health  =100

    @abstractmethod
    def is_alive(self):
        pass

    @abstractmethod
    def relax(self):
        pass

    @abstractmethod
    def attack(self,enemy):
        pass

    @abstractmethod
    def take_damage(self,damage):
        pass

    def is_alive(self):
        if self.health <= 0 : print(f"{self.name} повержен!")
        return self.health > 0


# Класс Fighter
class Fighter(Actor) :
    def __init__(self, name, weapon):
        super().__init__(name)
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f"{self.name} сменил оружие на {self.weapon.__class__.__name__}.")

    def attack(self,enemy):
        damage = self.weapon.attack()
        print(f"{self.name} "+self.weapon.explain(damage) )
        return damage

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name}  ранен и потерял  {damage}% крови! Только {self.health}% осталось ")

    def relax(self):
        self.health = ( self.health+100 )//2
        print(f"{self.name} подкрепился. Сила выросла до {self.health} % ")


# Класс Monster
class Monster(Actor):

    def attack(self,enemy):
        damage = random.randint(5, 15)  # Урон от монстра
        print(f"{self.name} кусает {enemy.name} на  {damage} дюймов ! " )
        return damage

    def take_damage(self, damage):
        effect = damage/self.skin()
        self.health = max(0, self.health - effect)
        print(f"{self.name} получил {effect} урона! Осталось здоровья: {self.health}")

    def relax(self):
        self.health = ( 3*self.health+100 )//4
        print( f"{self.name} зализывает раны. Силы выросли  до {self.health} " )

    def skin(self):
        return 2

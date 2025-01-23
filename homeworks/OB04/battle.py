from actor import *

# =====================  Моделирование  боя =================================
def battle(fighter, monster):
    print(f"Бой начался между {fighter.name} и {monster.name}!\n")
    actors = [fighter,monster]

    while True:
        for i,a in enumerate(actors):
            if a.is_alive():
                actors[1-i].take_damage( a.attack(actors[1-i]))
            else:
                return

# Восстановление сил для следующего боя
def time_out(fighter, monster):
    print("Истощенные противники восстанавливают силы")
    for x in [ fighter,monster] : x.relax()


# Создание бойца с мечом
fighter = Fighter("Фродо", Sword())
# Создание монстра
monster = Monster("Гоблин")

# первый бой
battle(fighter, monster)

# Смена оружия, восстановление  и новый бой
time_out( fighter, monster)
fighter.change_weapon(Bow())
battle(fighter, monster)


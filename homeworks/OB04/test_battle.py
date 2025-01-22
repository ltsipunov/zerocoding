from battle import *

# Создание бойца с мечом
fighter = Fighter("Ланселот", Sword())
# Создание монстра
monster = Monster("Гоблин")

battle(fighter, monster)

# Смена оружия и новый бой
time_out( fighter, monster)
fighter.change_weapon(Bow())
battle(fighter, monster)


from battle import *
# Основной блок

# Создание бойца с мечом
fighter_name = input("Введите имя бойца: ")
fighter = Fighter(fighter_name, Sword())

    # Создание монстра

monster = Monster("Гоблин")

# Бой
battle(fighter, monster)

# Смена оружия и новый бой
fighter.change_weapon(Bow())
print("\n--- Новый бой с тем же монстром ---\n")
battle(fighter, monster)

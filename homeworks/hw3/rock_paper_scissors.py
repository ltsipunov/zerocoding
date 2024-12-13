import random


def get_user_choice():
    user_input = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
    while user_input not in ["камень", "ножницы", "бумага"]:
        user_input = input("Неверный ввод. Пожалуйста, введите камень, ножницы или бумага: ").lower()
    return user_input


def get_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
            (user_choice == "ножницы" and computer_choice == "бумага") or \
            (user_choice == "бумага" and computer_choice == "камень"):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"


def play_game():
    user_wins = 0
    computer_wins = 0

    while user_wins < 3 and computer_wins < 3:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nВы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "Вы выиграли!":
            user_wins += 1
        elif result == "Компьютер выиграл!":
            computer_wins += 1

        print(f"\nСчет: Вы {user_wins} - {computer_wins} Компьютер")

    if user_wins == 3:
        print("\nПоздравляем! Вы победили в игре!")
    else:
        print("\nКомпьютер победил. Попробуйте снова!")


if __name__ == "__main__":
    play_game()
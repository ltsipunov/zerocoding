import requests
from bs4 import BeautifulSoup
from googletrans import Translator
translator = Translator()


# Создаём функцию, которая будет получать информацию
def get_words(src = 'en',dest = 'ru'):
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        random_words = soup.find("div", id="random_word").text.strip()
        translated = translator.translate(random_words,src=src, dest=dest)
        word = translated.text.lower()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        definition = translator.translate(word_definition,src=src, dest=dest).text
        # Чтобы программа возвращала словарь
        res = {
            "word": word,
            "definition": definition
        }
        return res
    # Функция, которая сообщит об ошибке, но не остановит программу
    except Exception as e:
        print("Произошла ошибка")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_words()
        word = word_dict.get("word")
        word_definition = word_dict.get("definition")

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user.lower() == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n или да/нет  ")
        if play_again[0] not in  ["y",'д' ]:
            print("Спасибо за игру!")
            break


word_game()
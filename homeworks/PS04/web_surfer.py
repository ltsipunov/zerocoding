from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import keyboard
import time

# Инициализация colorama для цветного текста в терминале
init()

# Переменная для хранения ссылок текущего параграфа
current_references = []


def get_page_source(url):
    """Загружает веб-страницу по URL и возвращает HTML-код."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Запуск браузера в режиме headless (без интерфейса)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()  # Укажите путь к chromedriver, если не установлен в PATH
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    time.sleep(3)  # Ждем загрузки страницы

    html_content = driver.page_source
    driver.quit()  # Закрываем браузер
    return html_content


def extract_paragraphs(html_content):
    """Извлекает параграфы (<p> теги) из HTML-контента."""
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = soup.find_all('p')  # Ищем все теги <p>
    return paragraphs


def display_paragraph(paragraph):
    """
    Выводит параграф в консоль с подсветкой ссылок (гиперссылки зеленым),
    а также сохраняет ссылки и их текст в переменную current_references.
    """
    global current_references
    current_references = []  # Очищаем список для каждой новой итерации

    for element in paragraph.contents:
        if element.name == 'a':  # Если это ссылка
            link_text = element.get_text()
            link_href = element.get('href')
            current_references.append({'text': link_text, 'href': link_href})

            # Печатаем ссылку зеленым цветом
            print(Fore.GREEN + link_text + Style.RESET_ALL, end='')
        else:  # Если это обычный текст
            print(element.text, end='')
    print('\n')  # Разделение между параграфами


def main():
    # URL целевой страницы
    # url = input("Введите URL страницы: ")
    url = 'https://en.wikipedia.org/wiki/Tau_Ceti_f'
    # Загружаем страницу и извлекаем HTML-контент
    html_content = get_page_source(url)

    # Извлекаем параграфы из HTML-содержимого
    paragraphs = extract_paragraphs(html_content)

    if not paragraphs:
        print("На странице не найдено параграфов.")
        return

    # Индекс текущего параграфа
    current_paragraph_index = 0
    total_paragraphs = len(paragraphs)

    display_paragraph(paragraphs[current_paragraph_index])

    # Основной цикл управления
    while True:
        if keyboard.is_pressed('down'):  # Клавиша "стрелка вниз"
            current_paragraph_index += 1
            if current_paragraph_index >= total_paragraphs:
                current_paragraph_index = total_paragraphs - 1
                print("Достигнут конец страницы.")
            else:
                display_paragraph(paragraphs[current_paragraph_index])
            time.sleep(0.2)  # Задержка для предотвращения повторяющихся нажатий

        if keyboard.is_pressed('up'):  # Клавиша "стрелка вверх"
            current_paragraph_index -= 1
            if current_paragraph_index < 0:
                current_paragraph_index = 0
                print("Вы на самом верху страницы.")
            else:
                display_paragraph(paragraphs[current_paragraph_index])
            time.sleep(0.2)  # Задержка для предотвращения повторяющихся нажатий

        if keyboard.is_pressed('esc'):  # Клавиша "ESC" для выхода
            print("Выход из программы...")
            break

        if keyboard.is_pressed('space'):  # Клавиша "ESC" для выхода
            print(f"""
            Current eferences:       
            {current_references}
                  """)

if __name__ == '__main__':
    main()
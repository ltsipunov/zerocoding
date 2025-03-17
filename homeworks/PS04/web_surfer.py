from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
import keyboard
import time

from colorama import init
from locator import Locator
# Инициализация colorama для цветного текста в терминале
init()

def main():
    url = 'https://en.wikipedia.org/wiki/Tau_Ceti'
    locator = Locator(url)
    if locator.max_para==0:
        print("На странице не найдено параграфов.")
        return

    while True: # ========================= MAIN CONTROL LOOP =====================================
        if keyboard.is_pressed('down'):
            locator.next_para(1)
            locator.load_para()
            locator.display_para()
            time.sleep(0.2)  # Задержка для предотвращения повторяющихся нажатий

        if keyboard.is_pressed('up'):  # Клавиша "стрелка вверх"
            locator.next_para(-1)
            locator.load_para()
            locator.display_para()
            time.sleep(0.2)  # Задержка для предотвращения повторяющихся нажатий

        if keyboard.is_pressed('left'):  # "влево - пред. ссылка"
            locator.next_link(-1)
            locator.display_para()
            time.sleep(0.2)  # Задержка для предотвращения повторяющихся нажатий

        if keyboard.is_pressed('right'):  # "влево - пред. ссылка"
            locator.next_link(1)
            locator.display_para()
            time.sleep(0.2)  # Задержка для предотвращения повторяющихся нажатий

        if keyboard.is_pressed('esc'):  # Клавиша "ESC" для выхода
            locator.close()
            print("Выход из программы...")
            break

        if keyboard.is_pressed('space'):  # Клавиша "ESC" для выхода
            print(f"""
            Current references:       
            {locator.links}
                  """)

if __name__ == '__main__':
    main()
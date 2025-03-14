import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from colorama import Fore, Style, init


class Locator:
    def __init__(self,link,driver=webdriver.Chrome ):
        self.link = link
        self.driver = driver()
        self.i_para, self.i_link = 0,0
        self.links,self.paras = [],[]
        self.min_para,self.max_para = 0,len(self.paras)
        self.min_link,self.max_link = 0,len(self.links)
        self.load_link()

    def load_link(self):
        self.driver.get(self.link)
        self.paras = self.driver.find_elements(By.TAG_NAME, "p")
        self.max_para = len(self.paras)
        print(f" {self.max_para} paragraphs loaded")

    def load_para(self):
        self.links = self.cur_para().find_elements(By.TAG_NAME, "a")
        self.max_link = len(self.links)

    def cur_para(self):
        return self.paras[self.i_para]

    def next_para(self,step=1):
        self.i_para = min( max( self.i_para + step,self.max_para),self.min_para)
        print(f" {self.max_link} links loaded")

    def next_link(self,step=1):
        self.i_link = min( max( self.i_link + step,self.max_link),self.min_link)

    def display_para(self):
        print( self.cur_para().text)
        # cur_link = 0
        # para = self.cur_para()
        # elements = para.find_elements()
        # for element in elements : # self.cur_para().find_elements():
        #     if element.tag_name == 'a':
        #         color_tag = Fore.YELLOW if cur_link==self.i_link  else  Fore.GREEN
        #         cur_link += 1
        #         print(color_tag + element.text + Style.RESET_ALL, end='')
        #     else:  # Если обычный текст
        #         print(element.text, end='')
        print('\n')

    def close(self):
        print('Close browser')
        self.driver.quit()
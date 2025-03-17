import time
import re

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
        self.min_para,self.max_para = 0,len(self.paras)-1
        self.min_link,self.max_link = 0,len(self.links)-1
        self.load_link()

    def load_link(self):
        self.driver.get(self.link)
        self.paras = self.driver.find_elements(By.TAG_NAME, "p")
        self.max_para = len(self.paras)
        print(f" {self.max_para} paragraphs loaded")

    def load_para(self):
        self.links = self.cur_para().find_elements(By.TAG_NAME, "a")
        self.links = [ el for el in self.links if el.accessible_name[0] != '[']
        self.i_link,self.max_link = self.min_link,len(self.links)-1

    def cur_para(self):
        return self.paras[self.i_para]

    def next_para(self,step=1):
        self.i_para = max( min( self.i_para + step,self.max_para),self.min_para)
        print(f" {self.max_link} links loaded")

    def next_link(self,step=1):
        self.i_link = max( min( self.i_link + step,self.max_link),self.min_link)
        pass

    def display_para(self):
        para_text=  Fore.WHITE+self.cur_para().text
        for j_link,e_link in enumerate(self.links):
            color_tag = Fore.YELLOW if j_link == self.i_link else Fore.GREEN
            para_text=para_text.replace(e_link.text,color_tag+e_link.text+Fore.WHITE,1)
        print(para_text+'\n')

    def close(self):
        print('Close browser')
        self.driver.quit()
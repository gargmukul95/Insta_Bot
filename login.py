import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as b


class Login:
    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(5)
        uid = self.driver.find_element_by_css_selector('#react-root > section > main > div > article > div > '
                                                       'div:nth-child(1) > div > form > div:nth-child(2) > div > '
                                                       'label > input')
        uid.send_keys(self.username)
        time.sleep(3)
        pswd = self.driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input')
        pswd.send_keys(self.password)
        time.sleep(3)
        btn = self.driver.find_element_by_css_selector('#react-root > section > main > div > article > div > '
                                                       'div:nth-child(1) > div > form > div:nth-child(4)')
        btn.click()
        time.sleep(3)
        not_now = self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
        not_now.click()
        time.sleep(3)

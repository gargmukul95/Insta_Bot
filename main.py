import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as b
import login

driver = 0


def main():
    global driver
    username = "username"
    password = "password"
    print('running scripts')
    driver = webdriver.Chrome('C:/Users/User/Desktop/Bluetown/chromedriver.exe')
    l = login.Login(driver, username, password)
    l.login()


if __name__ == '__main__':
    main()

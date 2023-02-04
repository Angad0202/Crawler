import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service('drivers/chromedriver')
browser = webdriver.Chrome(service=service)

def open_page(url: str):
    browser.get(url)

def close_browser():
    browser.close()

def add_input(by: By, value: str, text: str):
    field = browser.find_element(by=by, value=value)
    field.send_keys(text)
    time.sleep(1)

def click_button(by: By, value: str):
    button = browser.find_element(by=by, value=value)
    button.click()
    time.sleep(1)

def login(UserID: str, password: str):
    add_input(by=By.ID, value='email', text=UserID)
    add_input(by=By.ID, value='Pwd', text=password)
    browser.find_element(by=By.ID, value='Pwd').send_keys(Keys.ENTER)

def go_to_sap():
    sap_link = browser.find_element(By.XPATH, "//a[@class='nav-link video-btnsapportal']")
    sap_link.click()
    time.sleep(5)
    click_button(by=By.ID,value="btnmySAPPortal")
    time.sleep(30)
    timetable_link = browser.find_element(By.XPATH, "//td[@id='WD0223']/a[@id='WD0224']")
    timetable_link.click()
    time.sleep(20)

if __name__ == '__main__':
    open_page('https://myupes.upes.ac.in/Login')
    login(UserID='500082940@stu.upes.ac.in', password='WeJ5TW5G@1')
    time.sleep(3)
    go_to_sap()
    time.sleep(200)
    close_browser()

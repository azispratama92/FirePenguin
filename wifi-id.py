# Script AutoLogin Wifi ID oleh Azis R. Pratama
# Modifikasi dari script autologin gmail oleh Hongkiat ==> Rujukan lamat GitHub 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = '80615524601'
passwordStr = '11034897135295'

browser = webdriver.Chrome()
browser.get(('http://wifi.id/'))

# comment here

username = browser.find_element_by_id('username_form')
username.send_keys(usernameStr)

# comment here if necessary

password = WebDriverWait(browser, 1).until(
    EC.presence_of_element_located((By.ID, 'password_form')))

password.send_keys(passwordStr)
 

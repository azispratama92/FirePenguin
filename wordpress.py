# Script AutoLogin Wifi ID oleh Azis R. Pratama
# Modifikasi dari script autologin gmail oleh Hongkiat 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'pratama'
passwordStr = 'rahasia'

browser = webdriver.Chrome()
browser.get(('http://127.0.0.1/wp-login.php?redirect_to=http%3A%2F%2F127.0.0.1%2Fwp-admin%2F&reauth=1'))

# isikan username voucher wifi ID Anda

username = browser.find_element_by_id('user_login')
username.send_keys(usernameStr)

# memberikan sedikit jeda 1 detik

password = WebDriverWait(browser, 1).until(
    EC.presence_of_element_located((By.ID, "user_pass")))

password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('wp-submit')
signInButton.click()

# Todo List: 

#!/usr/bin/python
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get('http://wifi.id/') #Here put your page login

elem = browser.find_elements_by_name('username_form') 
elem[1].send_keys('username') #here put your  username
elem = browser.find_elements_by_name('password_form') 
elem[1].send_keys('password' + Keys.RETURN) #here put your password

browser.quit()

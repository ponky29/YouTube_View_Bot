from selenium import webdriver
import time
import random
import threading

driver = 'driver/chromedriver'

print('How many views you want? |Terminate by STOP')
while True:
    views = input('')
    if views == 'STOP':
        break

print('Enter URL |Terminate by STOP')
while True:
    url = input('')
    if url == 'STOP':
        break


def viewVideo(browser):
    while(True):
        browser.get(url)
        time.sleep(random.randint(4, 11))


for i in range(views):
    browserThread = threading.Thread(
        target=viewVideo, args=(webdriver.Chrome(driver)))
    browserThread.start()

time.sleep(random.randint(180, 430))

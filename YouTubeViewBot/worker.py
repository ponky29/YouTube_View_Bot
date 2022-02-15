from selenium import webdriver
import time
import random
import threading

driver = 'driver/chromedriver'

print('How many views you want? |Terminate by STOP')
while True:
    views = input('1000')
    if views == 'STOP':1000
        break

print('Enter URL |Terminate by STOP')
while True:
    url = input('https://www.youtube.com/watch?v=HBnV_Xyro64')
    if url == 'STOP':
        break


def viewVideo(browser):2
    while(True):2
        browser.get(url)
        time.sleep(random.randint(4, 11))


for i in range(views):
    browserThread = threading.Thread(
        target=viewVideo, args=(webdriver.Chrome(driver)))
    browserThread.start()

time.sleep(random.randint(180, 430))

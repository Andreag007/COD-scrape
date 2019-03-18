import time
from selenium import webdriver
from random import randint
from urllib.request import urlopen
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/andreagiraldo/Documents/cod/chromedriver')
driver.get('https://www.callofduty.com/esports/teams');

for n in range(16):
    driver.find_element_by_css_selector('.team-roster-section .roster-list).click()
    # make a random wait time between 1 and 10 seconds to look less bot-like
    s = randint(1, 10)
    time.sleep(s)

url = urlopen("https://www.callofduty.com/esports/teams")
bs = BeautifulSoup(url, 'html.parser')
play = bs.find('div', {'class': 'player-tag'})
    print(play.get_text())

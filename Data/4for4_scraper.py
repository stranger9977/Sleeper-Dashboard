from pprint import pprint

import requests
import json
import bs4
import pandas as pd
import html5lib
import os
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from json import JSONDecoder

# from user_agent import random_header
pd.set_option("display.max_columns", 99)
pd.set_option("display.max_columns", 99)





# set url
url = 'https://www.4for4.com/'

driver.get(url)
username = 'nick.gurol'
password = "22eTyS8JUx!fben"
# # login to website
driver.find_element(By.ID, "user_login").send_keys(username)
driver.find_element(By.ID, "user_pass").send_keys(password)
driver.find_element(By.ID, "wp-submit").click()

# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
driver.get('https://establishtherun.com/etrs-top-300-for-underdogfantasy/')

page_source = driver.page_source

soup = page_source

df = pd.read_html(driver.page_source, index_col='Player',flavor='html5lib')[0]

print(df)


from datetime import datetime
df.to_csv(f'/Users/nick/Sleeper-Dashboard/Data/etr_underdog_rankings-{datetime.now():%Y-%m-%d}.csv')




# df = pd.read_html(str(table))[0]
# df = df.iloc[:, 1:]
# print(df.head())






from pprint import pprint
from urllib.parse import urljoin
from urllib.request import urlretrieve

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

options = webdriver.ChromeOptions()

preferences = {'download.default_directory': '/Users/nick/Sleeper-Dashboard/Data'}

options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

# set url
url = 'https://www.4for4.com/'
driver.get(url)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[4]/div/div[1]/div/div/div/a").click()
username = 'nickgurol@gmail.com'
password = "2UbJ4W!jVLGurWW"
# # login to website
driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/form/div/div[3]/input").send_keys(username)
driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/form/div/div[4]/input").send_keys(password)
driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/form/div/div[5]/input").click()

url2 = 'https://www.4for4.com/full-impact/cheatsheet/QB/60444/ff_nflstats_early'

driver.get(url2)
# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

driver.get(url2)

time.sleep(10)

driver.find_element(By.XPATH,
                    "/html/body/div[4]/div/div[3]/div/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/a").click()
time.sleep(5)
# df = pd.read_html(str(table))[0]
# df = df.iloc[:, 1:]
# print(df.head())

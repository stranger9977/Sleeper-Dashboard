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
url = 'https://www.cbssports.com/login?product_abbrev=mgmt&xurl=https%3A%2F%2Fwhitey.football.cbssports.com%2F&master_product=39258'
driver.get(url)


username = 'nickgurol@gmail.com'
password = "6iaVy5!xtd6P5%X"
# # login to website
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/form/div[1]/div[1]/div[1]/div/div[1]/div/input").send_keys(username)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/form/div[1]/div[1]/div[2]/div/div[1]/div/input").send_keys(password)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/form/div[1]/div[2]/input").click()

url2 = 'https://whitey.football.cbssports.com/draft/results/2021:Pre-season:Pre-season'

driver.get(url2)
# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'"))

driver.get(url2)



driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[5]/div/button[2]").click()


# df = pd.read_html(str(table))[0]
# df = df.iloc[:, 1:]
# print(df.head())

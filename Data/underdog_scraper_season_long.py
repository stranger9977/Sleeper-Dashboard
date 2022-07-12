import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from urllib.parse import urljoin  # for Python2: from urlparse import urljoin
from urllib.request import urlretrieve

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

pd.set_option("display.max_columns", 99)
pd.set_option("display.max_columns", 99)





# set url
url = 'https://underdogfantasy.com/login'

driver.get(url)
username = 'nickgurol@gmail.com'
password = "Spiderm@n99"
# # login to website
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/label/div[2]/input").send_keys(username)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[2]/label/div[2]/input").send_keys(password)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/form/button").click()

# wait the ready state to be complete
driver.get('https://underdogfantasy.com/rankings/nfl/f659a9be-fd34-4a1e-9c43-0816267e603d')

time.sleep(20)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[3]/button").click()

csv_url = urljoin(url + "/", driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/a").get_attribute("href"))
from datetime import datetime
urlretrieve(csv_url,  f"underdog_adp-{datetime.now():%Y-%m-%d}.csv")




# df = pd.read_html(str(table))[0]
# df = df.iloc[:, 1:]
# print(df.head())






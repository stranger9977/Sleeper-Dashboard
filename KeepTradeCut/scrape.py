#this program will scrape values from keeptradecut and clean the data set for modeling
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://keeptradecut.com/dynasty-rankings'    
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="rankings-page-rankings")
players = results.find_all("div", class_="onePlayer")

name_list = []
value_list = []
for player in players: 
    name = (player.find("p", class_="player-name").text.strip())
    value = (player.find("p", class_="value").text.strip())
    name_list.append(name)
    value_list.append(value)
Player_lists_to_dicts = {"Player": name_list, 'KTC Value': value_list}

df = pd.DataFrame(Player_lists_to_dicts)
from datetime import datetime
df.to_csv(f'/Users/nick/Desktop/FantasyDashboard/KeepTradeCut/scrape-{datetime.now():%Y-%m-%d}.csv', index = False)






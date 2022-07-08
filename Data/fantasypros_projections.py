"""
Quicky script to scrape projections from fantasypros.com
"""
from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'http://www.fantasypros.com/nfl/projections'
url_flex = 'https://www.fantasypros.com/nfl/projections/flex.php?week=draft&scoring=HALF&week=draft'
page = requests.get(url)
if page.ok:
    print('Response was OK!')
soup = BeautifulSoup(page.content, "html.parser")
data = soup.find('table')
table_rows = data.find_all('tr')
l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    l.append(row)
df = pd.DataFrame(l)
df = df.iloc[2:, :]

df.rename(columns={0: 'Player',
                   1: 'PassAtt',
                   2: 'Cmp',
                   3: 'PassYds',
                   4: 'PassTds',
                   5: 'PassInts',
                   6: 'RushAtt',
                   7: 'RushYds',
                   8: 'RushTds',
                   9: 'FL',
                   10: 'FPTS',
                   }, inplace=True)

df['FirstName'] = df['Player'].str.split(' ').str[0]
df['LastName'] = df['Player'].str.split(' ').str[1]

df['Player'] = df['FirstName'] + " " + df['LastName']

qb_df = df[['Player','PassAtt','Cmp','PassYds', 'PassTds','PassInts','RushAtt','RushYds', 'RushTds','FL','FPTS']]
# get flex fantasy points
page = requests.get(url_flex)
if page.ok:
    print('Response was OK!')
soup = BeautifulSoup(page.content, "html.parser")
data = soup.find('table')
table_rows = data.find_all('tr')
l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    l.append(row)
df = pd.DataFrame(l)
df = df.iloc[2:, :]

df.rename(columns={0: 'Player',
                   1: 'Pos',
                   2: 'RushAtt',
                   3: 'RushYds',
                   4: 'RushTds',
                   5: 'Rec',
                   6: 'RecYds',
                   7: 'RecTds',
                   8: 'FL',
                   9: 'FPTS'
                   }, inplace=True)

df['FirstName'] = df['Player'].str.split(' ').str[0]
df['LastName'] = df['Player'].str.split(' ').str[1]

df['Player'] = df['FirstName'] + " " + df['LastName']
flex_df = df[['Player','RushAtt','RushYds', 'RushTds', 'Rec','RecYds', 'RecTds','FL','FPTS']]
expert_df = pd.concat([qb_df, flex_df])
expert_df = expert_df.fillna(0)
expert_df['RushYds'] = expert_df['RushYds'].str.replace(',', '').astype(float)
expert_df['PassYds'] = expert_df['PassYds'].str.replace(',', '').astype(float)
expert_df['RecYds'] = expert_df['RecYds'].str.replace(',', '').astype(float)
expert_df = expert_df.fillna(0)
expert_df[['PassAtt', 'Cmp', 'PassTds', 'PassInts', 'RushAtt', 'RushTds', 'FL', 'FPTS', 'Rec',
       'RecTds']]= expert_df[['PassAtt', 'Cmp', 'PassTds', 'PassInts', 'RushAtt', 'RushTds', 'FL', 'FPTS', 'Rec',
       'RecTds']].astype(float)

print(expert_df.info(verbose=True))
from datetime import datetime

expert_df.to_csv(f'/Users/nick/Sleeper-Dashboard/Data/expert_consensus_projections-{datetime.now():%Y-%m-%d}.csv', index=False)


from tabnanny import verbose
from numpy import place
import pandas as pd 
from sleeper_wrapper import League
import requests
from datetime import datetime

from sleeper_wrapper import League
league = League(784453846419283968)# enter your league id here 

dynasty_process_player_values_df = pd.read_csv(f'/Users/nick/Desktop/FantasyDashboard/DynastyProcess/player_values-{datetime.now():%Y-%m-%d}.csv')
dynasty_process_pick_values_df = pd.read_csv(f'/Users/nick/Desktop/FantasyDashboard/DynastyProcess/pick_values-{datetime.now():%Y-%m-%d}.csv')
sleeper_players_df = pd.read_csv(f'/Users/nick/Desktop/FantasyDashboard/Sleeper/players-{datetime.now():%Y-%m-%d}.csv')
sleeper_rosters_df = pd.read_csv(f'/Users/nick/Desktop/FantasyDashboard/Sleeper/rosters-{datetime.now():%Y-%m-%d}.csv')
keep_trade_cut_player_and_pick_values_df = pd.read_csv(f'/Users/nick/Desktop/FantasyDashboard/KeepTradeCut/scrape-{datetime.now():%Y-%m-%d}.csv')

#trim for needed colulmns

dynasty_process_player_values_df = dynasty_process_player_values_df[['sleeper_id','player', 'pos','team', 'age', 'value_1qb', 'value_2qb', 'scrape_date' ]]
dynasty_process_pick_values_df = dynasty_process_pick_values_df[['player', 'pos' ]]
sleeper_rosters_df = sleeper_rosters_df[['player_id', 'players']]



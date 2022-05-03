from sleeper_wrapper import League
league = League(784453846419283968)# enter your league id here 
league_last_year = League(650031553094725632)# this is for last year standings during the offseason
import pandas as pd

#don't run this more than once a day! 
from sleeper_wrapper import Players

players = Players()
players = players.get_all_players()
players_df = pd.DataFrame(players)

from datetime import datetime
players_df = players_df.transpose()
players_df.to_csv('/Users/nick/Desktop/FantasyDashboard/Sleeper/players.csv', index = False)

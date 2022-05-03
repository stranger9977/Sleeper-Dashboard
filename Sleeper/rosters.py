#update with your league url
from sleeper_wrapper import League
league = League(784453846419283968)# enter your league id here 
league_last_year = League(650031553094725632)# this is for last year standings during the offseason

rosters = league_last_year.get_rosters()
users = league_last_year.get_users()

roster = league.get_rosters()

#Bring in different dataframes to be merged later
import pandas as pd

rosters = league.get_rosters()
rosters_df = pd.DataFrame(rosters)

users = league.get_users()
users_df = pd.DataFrame(users)

draft = league.get_traded_picks()
draft_df = pd.DataFrame(draft)

#merging for display names
rosters_df_trim = rosters_df[['owner_id', 'roster_id', 'players']]
users_df_trim = users_df[['user_id','display_name']]

rosters_df = rosters_df_trim.merge(users_df_trim, left_on= 'owner_id', right_on='user_id')
 
rosters_df = rosters_df[['display_name', 'user_id','roster_id', 'players']]
rosters_df = rosters_df.rename(columns = {"players": "player_id"})
rosters_df = rosters_df.explode('player_id').reset_index(drop=True)

# placing players on teams
from datetime import datetime

players_df_raw = pd.read_csv('/Users/nick/Desktop/FantasyDashboard/Sleeper/players.csv')

players_df = players_df_raw[['player_id','full_name','position','team','age']]

rosters_df = rosters_df.merge(players_df, how='left', on=['player_id'])


from datetime import datetime
rosters_df.to_csv('/Users/nick/Desktop/FantasyDashboard/Sleeper/rosters.csv', index = False)





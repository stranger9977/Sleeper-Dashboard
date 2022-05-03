from importlib_metadata import Sectioned
from matplotlib.pyplot import draw_if_interactive
import pandas as pd

from sleeper_wrapper import League
import numpy as np
import requests

#import league. This step will eventually allow us to inport any league or user id.
league = League(784453846419283968)

#pulling in rosters from sleeper/
rosters = league.get_rosters()
rosters_df = pd.DataFrame(rosters)


#pulling in the user data and ids. 
users = league.get_users()
users_df = pd.DataFrame(users)

# #merging for display names
rosters_df_trim = rosters_df[['owner_id', 'roster_id']]
users_df_trim = users_df[['user_id','display_name']]

rosters_df = rosters_df_trim.merge(users_df_trim, left_on= 'owner_id', right_on='user_id')
 
rosters_df = rosters_df[['display_name', 'user_id','roster_id']]

rosters_display_name = rosters_df[['display_name', 'user_id','roster_id']]

rosters_df = rosters_df_trim.merge(users_df_trim, left_on= 'owner_id', right_on='user_id')




# #getting the draft order 


response = requests.get("https://api.sleeper.app/v1/draft/784453846419283969")

draft_order = response.json()["draft_order"]


draft_order_df = pd.DataFrame.from_dict(draft_order, orient='index', columns = ['Pick'])

# #combining draft order with rosters 
picks_df = rosters_df.merge(draft_order_df, left_on= 'owner_id', right_index=True)

picks_df = picks_df.sort_values(by = ['Pick'])



# #generating a repeating list for the draft order for a period of 3 years 
draft_order_list = []

for i in range(15):
    for index, row in picks_df.iterrows():
        r = row.to_dict()
        draft_order_list.append(r)

    draft_order_df =  pd.DataFrame(draft_order_list)

#adding a column that shows the pick number from 1 to 180 (three full years of drafts)
draft_order_df['range'] = pd.Series(range(1,181)).astype(int)

from datetime import date

#add a column with the year 
def year(row): 
    if row['range'] > 0 and row['range'] <= 60:
        return date.today().year
    elif row['range'] > 60 and row['range'] <= 120:
        return date.today().year+1
    elif row['range'] > 120  and row['range'] <= 180:
        return date.today().year+2

# # add a column with the round 
def round(row): 
    if row['range'] > 0 and row['range'] <= 12:
        return "1"
    elif row['range'] > 12 and row['range'] <= 24:
        return "2"
    elif row['range'] > 24  and row['range'] <= 36:
        return "3"
    elif row['range'] > 36  and row['range'] <= 48:
        return "4"
    elif row['range'] > 48  and row['range'] <= 60:
        return "5"
    if row['range'] > 60 and row['range'] <= 72:
        return "1"
    elif row['range'] > 72 and row['range'] <= 84:
        return "2"
    elif row['range'] > 84  and row['range'] <= 96:
        return '3'
    elif row['range'] > 96  and row['range'] <= 108:
        return '4'
    elif row['range'] > 108  and row['range'] <= 120:
        return '5'
    if row['range'] > 120 and row['range'] <= 132:
        return '1'
    elif row['range'] > 132 and row['range'] <= 144:
        return '2'
    elif row['range'] > 144  and row['range'] <= 156:
        return '3'
    elif row['range'] > 156  and row['range'] <= 168:
        return '4'
    elif row['range'] > 160  and row['range'] <= 180:
        return '5'


draft_order_df['Year'] = draft_order_df.apply(lambda row: year(row), axis=1)
draft_order_df['Round'] = draft_order_df.apply(lambda row: round(row), axis = 1)

# adds a zero to the picknumber 
draft_order_df["pick_concat"] = draft_order_df.Pick.map("{:02}".format)

draft_order_df['player'] = draft_order_df['Year'].astype(str) + " " + "Pick" + " " + draft_order_df['Round'] + "." + draft_order_df['pick_concat']

# creating a table with the original owner id and the year and round of the pick 
draft_order_df = draft_order_df[['roster_id', 'display_name','Year', 'Round','Pick', 'range']]


draft_order_df = draft_order_df.rename(columns={'roster_id':'original_owner_id' })
draft_order_df['new_owner_id'] = draft_order_df['original_owner_id']


trade = league.get_traded_picks()
trade_df = pd.DataFrame(trade)
# print(draft_order_df)
# trade_df.to_csv('/Users/nick/Desktop/FantasyDashboard/Sleeper/traded_picks.csv', index_col=False)

# trade_df = pd.read_csv('/Users/nick/Desktop/FantasyDashboard/Sleeper/traded_picks.csv' , index_col=False )
# print(picks_df.head())
trade_shuffle_df = trade_df[['owner_id','roster_id','season', 'round']].astype(int)
trade_shuffle_df = trade_shuffle_df.rename(columns={'roster_id':'original_owner_id','owner_id':'new_owner_id', 'season':'Year','round':'Round'})
picks_df = picks_df.rename(columns={'roster_id': 'original_owner_id'})
picks_df['original_owner_id'] = picks_df['original_owner_id'].astype(int)
trade_shuffle_df['original_owner_id'] = trade_shuffle_df['original_owner_id'].astype(int)
picks_df=picks_df[['original_owner_id', 'display_name','Pick']]
trade_shuffle_df = trade_shuffle_df.merge(picks_df, how = 'left', on='original_owner_id')
# print(picks_df.dtypes)
# print(draft_order_df)
# print(trade_shuffle_df.head(40))
# print(picks_df.info(verbose=True))
# print(trade_shuffle_df.info(verbose=True))
# print(trade_shuffle_df)

draft_order_df['Round'] = draft_order_df['Round'].astype(int)

draft_order_df=draft_order_df[['original_owner_id', 'display_name', 'Year', 'Round', 'Pick','range']]
draft_trade_df = pd.merge(draft_order_df,trade_shuffle_df, on=['Year','Round','Pick'], how='left')


# do I need to add the drat order to this dataframe before merging? It think this will help me re order the picks. 

draft_trade_df.sort_values(by='range')



draft_trade_df['new_owner_id'].fillna(draft_trade_df['original_owner_id_x'], inplace=True)

draft_trade_df['display_name_y'].fillna(draft_trade_df['display_name_x'], inplace=True)


final_draft_order_df = draft_trade_df[['new_owner_id','Year','Round','Pick']]

final_draft_order_df = final_draft_order_df.rename(columns={'new_owner_id': 'roster_id'})
rosters_display_name = rosters_display_name[['roster_id','display_name']]
final_draft_order_df = final_draft_order_df.merge(rosters_display_name, how='left', on='roster_id')

#need tou seperate future picks out and reformat the strings so they match dynastyprocess values. I am so happy to be at this stage. 

final_draft_order_df.to_csv('/Users/nick/Desktop/FantasyDashboard/Sleeper.draft_order.csv')


player_values_df = pd.read_csv('https://raw.githubusercontent.com/dynastyprocess/data/master/files/values.csv')


player_values_df['position'] = player_values_df['pos'].astype(str)


player_values_df = player_values_df[player_values_df['player'].str.contains('Early | Late | Mid ') == False]
pick_values_df = player_values_df.loc[player_values_df['position'] =='PICK']

pick_values_df = pick_values_df[['player','position','value_1qb','value_2qb','scrape_date']]


final_draft_order_df["pick_concat"] = final_draft_order_df.Pick.map("{:02}".format)



year = date.today().year
this_year = str(year)
next_year = str(year + 1)
year_following = str(year + 2) 


final_draft_order_df = final_draft_order_df.astype(str)

def pick_names(row):
    if row['Year'] == next_year or row['Year'] == year_following:
        if row['Round'] == '1':
            return  row['Year'] + " " + row['Round'] + "st"
        if row['Round'] == '2':
            return  row['Year'] + " " + row['Round'] + "nd"
        if row['Round'] == '3':
            return  row['Year'] + " " + row['Round'] + "rd"
        if row['Round'] == '4':
            return  row['Year'] + " " + row['Round'] + "th"
        if row['Round'] == '5':
            return  row['Year'] + " " + row['Round'] + "th"
    elif row['Year'] == this_year:
        return row['Year'] + " " + "Pick" + " " + row['Round'] + "." + row['pick_concat']
        
final_draft_order_df['player'] = final_draft_order_df.apply(lambda row: pick_names(row), axis=1)



final_draft_order_df =final_draft_order_df[['roster_id','display_name','player']]

from datetime import datetime

pick_values_df = pd.merge(final_draft_order_df,pick_values_df, on='player', how='left')
print(pick_values_df.head())
pick_values_df.to_csv(f'/Users/nick/Desktop/FantasyDashboard/Sleeper/pick_values-{datetime.now():%Y-%m-%d}.csv', index = False)



# # # # future_picks_df = future_picks_df.sort_values(by=['ecr_1qb'])

# # # # # future_picks_df[['season', 'round']] = future_picks_df.player.str.split(' ', expand=True)
# # # # # future_picks_df['round'] = future_picks_df['round'].str[:1]


# # # # # # # pick_values_df = pd.concat([pick_values_df,future_picks_df], ignore_index=True)

# # # # # rosters_picks = pd.concat([draft_order_df, pick_values_df], axis=1)
# # # # # print(future_picks_df.info(verbose=True))






# # # # # # # # pick_values_df = pd.concat([draft_order_df, pick_values_df], axis=1)

# # # # # # # # pick_values_shuffle_df = pick_values_df[['roster_id', 'season_orig', 'round_orig']]




# # # # # # # # # from datetime import datetime
# # # # # # # from datetime import datetime



# # # # # # print(pick_values_shuffle_df)

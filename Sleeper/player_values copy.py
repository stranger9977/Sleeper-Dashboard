from importlib_metadata import Sectioned
import pandas as pd
import streamlit as st

from sleeper_wrapper import League
import numpy as np
import requests
st.set_page_config(page_title="Sleeper Dashboard") 


user_input = st.text_input("enter your league id here", 784453846419283968)

user_input

league_id = user_input

league = League(league_id)



# #dynasty_process_player_values
# df = pd.read_csv('https://raw.githubusercontent.com/dynastyprocess/data/master/files/values-players.csv')

# #ids to merge player values with sleeper ids
# id_df = pd.read_csv('https://raw.githubusercontent.com/dynastyprocess/data/master/files/db_playerids.csv')


# # pick_values_df = pd.read_csv('https://raw.githubusercontent.com/dynastyprocess/data/master/files/values-picks.csv')




# id_df = id_df[['fantasypros_id','sleeper_id']]
# values_df = pd.merge(df, id_df, how= 'left', left_on=['fp_id'], right_on=['fantasypros_id'])

# from datetime import datetime

# # values_df.to_csv(f'/Users/nick/Desktop/FantasyDashboard/DynastyProcess/player_values-{datetime.now():%Y-%m-%d}.csv', index = False)

# values_df = values_df.loc[values_df['pos'].isin(['QB', 'RB', 'WR', 'TE'])]

# values_df = values_df[['sleeper_id','value_1qb','value_2qb']]

# #getting the rosters and putting them with the display names 
# roster = league.get_rosters()

# rosters = league.get_rosters()
# rosters_df = pd.DataFrame(rosters)

# users = league.get_users()
# users_df = pd.DataFrame(users)



# #merging for display names
# rosters_df_trim = rosters_df[['owner_id', 'roster_id', 'players']]
# users_df_trim = users_df[['user_id','display_name']]

# rosters_df = rosters_df_trim.merge(users_df_trim, left_on= 'owner_id', right_on='user_id')
 
# rosters_df = rosters_df[['display_name', 'user_id','roster_id', 'players']]
# rosters_df = rosters_df.rename(columns = {"players": "player_id"})
# rosters_df = rosters_df.explode('player_id').reset_index(drop=True)

# # placing players on teams
# from datetime import datetime

# players_df_raw = pd.read_csv('/Users/nick/Desktop/FantasyDashboard/Sleeper/players-2022-04-28.csv')

# players_df = players_df_raw[['player_id','full_name','position','team','age']]

# rosters_df = rosters_df.merge(players_df, how='left', on=['player_id'])


# from datetime import datetime
# #pulling in rosters from sleeper/
# rosters = league.get_rosters()
# rosters_df = pd.DataFrame(rosters)


# #pulling in the user data and ids. 
# users = league.get_users()
# users_df = pd.DataFrame(users)

# # #merging for display names
# # rosters_df_trim = rosters_df[['owner_id', 'roster_id']]
# # users_df_trim = users_df[['user_id','display_name']]

# # rosters_df = rosters_df_trim.merge(users_df_trim, left_on= 'owner_id', right_on='user_id')
 
# # rosters_df = rosters_df[['display_name', 'user_id','roster_id']]

# # rosters_display_name = rosters_df[['display_name', 'user_id','roster_id']]

# # rosters_df = rosters_df_trim.merge(users_df_trim, left_on= 'owner_id', right_on='user_id')
# #rosters_df.to_csv(f'/Users/nick/Desktop/FantasyDashboard/Sleeper/rosters-{datetime.now():%Y-%m-%d}.csv', index = False)
# rosters_df = pd.read_csv('/Users/nick/Desktop/FantasyDashboard/Sleeper/rosters.csv')
# rosters_df = rosters_df.loc[rosters_df['position'].isin(['QB', 'RB', 'WR', 'TE'])]

# rosters_df['sleeper_id'] = rosters_df['player_id'].astype(float)

# roster_values_df = rosters_df.merge(values_df, how='left', on='sleeper_id')



# # import league. This step will eventually allow us to inport any league or user id.

# #pulling in rosters from sleeper/
# rosters = league.get_rosters()
# rosters_df = pd.DataFrame(rosters)


# #pulling in the user data and ids. 
# users = league.get_users()
# users_df = pd.DataFrame(users)

# # #merging for display names
# rosters_df_trim = rosters_df[['owner_id', 'roster_id']]
# users_df_trim = users_df[['user_id','display_name']]

# rosters_df = rosters_df_trim.merge(users_df_trim, left_on= 'owner_id', right_on='user_id')
 
# rosters_df = rosters_df[['display_name', 'user_id','roster_id']]

# rosters_display_name = rosters_df[['display_name', 'user_id','roster_id']]

# rosters_df = rosters_df_trim.merge(users_df_trim, left_on= 'owner_id', right_on='user_id')

# # #getting the draft order 

# response = requests.get("https://api.sleeper.app/v1/draft/784453846419283969")

# draft_order = response.json()["draft_order"]

# draft_order_df = pd.DataFrame.from_dict(draft_order, orient='index', columns = ['Pick'])

# # #combining draft order with rosters 
# picks_df = rosters_df.merge(draft_order_df, left_on= 'owner_id', right_index=True)

# picks_df = picks_df.sort_values(by = ['Pick'])

# # #generating a repeating list for the draft order for a period of 3 years 
# draft_order_list = []

# for i in range(15):
#     for index, row in picks_df.iterrows():
#         r = row.to_dict()
#         draft_order_list.append(r)

#     draft_order_df =  pd.DataFrame(draft_order_list)

# #adding a column that shows the pick number from 1 to 180 (three full years of drafts)
# draft_order_df['range'] = pd.Series(range(1,181)).astype(int)

# from datetime import date

# #add a column with the year 
# def year(row): 
#     if row['range'] > 0 and row['range'] <= 60:
#         return date.today().year
#     elif row['range'] > 60 and row['range'] <= 120:
#         return date.today().year+1
#     elif row['range'] > 120  and row['range'] <= 180:
#         return date.today().year+2

# # # add a column with the round 
# def round(row): 
#     if row['range'] > 0 and row['range'] <= 12:
#         return "1"
#     elif row['range'] > 12 and row['range'] <= 24:
#         return "2"
#     elif row['range'] > 24  and row['range'] <= 36:
#         return "3"
#     elif row['range'] > 36  and row['range'] <= 48:
#         return "4"
#     elif row['range'] > 48  and row['range'] <= 60:
#         return "5"
#     if row['range'] > 60 and row['range'] <= 72:
#         return "1"
#     elif row['range'] > 72 and row['range'] <= 84:
#         return "2"
#     elif row['range'] > 84  and row['range'] <= 96:
#         return '3'
#     elif row['range'] > 96  and row['range'] <= 108:
#         return '4'
#     elif row['range'] > 108  and row['range'] <= 120:
#         return '5'
#     if row['range'] > 120 and row['range'] <= 132:
#         return '1'
#     elif row['range'] > 132 and row['range'] <= 144:
#         return '2'
#     elif row['range'] > 144  and row['range'] <= 156:
#         return '3'
#     elif row['range'] > 156  and row['range'] <= 168:
#         return '4'
#     elif row['range'] > 160  and row['range'] <= 180:
#         return '5'


# draft_order_df['Year'] = draft_order_df.apply(lambda row: year(row), axis=1)
# draft_order_df['Round'] = draft_order_df.apply(lambda row: round(row), axis = 1)

# # adds a zero to the picknumber 
# draft_order_df["pick_concat"] = draft_order_df.Pick.map("{:02}".format)

# draft_order_df['player'] = draft_order_df['Year'].astype(str) + " " + "Pick" + " " + draft_order_df['Round'] + "." + draft_order_df['pick_concat']

# # creating a table with the original owner id and the year and round of the pick 
# draft_order_df = draft_order_df[['roster_id', 'display_name','Year', 'Round','Pick', 'range']]

# #keeping track of the trade
# draft_order_df = draft_order_df.rename(columns={'roster_id':'original_owner_id' })
# draft_order_df['new_owner_id'] = draft_order_df['original_owner_id']

# #bringing in the traded picks
# trade = league.get_traded_picks()
# trade_df = pd.DataFrame(trade)
# #merging the draft order I geneerated with the picks to edit the dataframe
# trade_shuffle_df = trade_df[['owner_id','roster_id','season', 'round']].astype(int)
# trade_shuffle_df = trade_shuffle_df.rename(columns={'roster_id':'original_owner_id','owner_id':'new_owner_id', 'season':'Year','round':'Round'})
# picks_df = picks_df.rename(columns={'roster_id': 'original_owner_id'})
# picks_df['original_owner_id'] = picks_df['original_owner_id'].astype(int)
# trade_shuffle_df['original_owner_id'] = trade_shuffle_df['original_owner_id'].astype(int)
# picks_df=picks_df[['original_owner_id', 'display_name','Pick']]
# trade_shuffle_df = trade_shuffle_df.merge(picks_df, how = 'left', on='original_owner_id')


# draft_order_df['Round'] = draft_order_df['Round'].astype(int)

# draft_order_df=draft_order_df[['original_owner_id', 'display_name', 'Year', 'Round', 'Pick','range']]
# draft_trade_df = pd.merge(draft_order_df,trade_shuffle_df, on=['Year','Round','Pick'], how='left')


# # do I need to add the drat order to this dataframe before merging? It think this will help me re order the picks. 

# draft_trade_df.sort_values(by='range')



# draft_trade_df['new_owner_id'].fillna(draft_trade_df['original_owner_id_x'], inplace=True)

# draft_trade_df['display_name_y'].fillna(draft_trade_df['display_name_x'], inplace=True)


# final_draft_order_df = draft_trade_df[['new_owner_id','Year','Round','Pick']]

# final_draft_order_df = final_draft_order_df.rename(columns={'new_owner_id': 'roster_id'})
# rosters_display_name = rosters_display_name[['roster_id','display_name']]
# final_draft_order_df = final_draft_order_df.merge(rosters_display_name, how='left', on='roster_id')

# #need tou seperate future picks out and reformat the strings so they match dynastyprocess values. I am so happy to be at this stage. 

# # final_draft_order_df.to_csv('/Users/nick/Desktop/FantasyDashboard/Sleeper/draft_order.csv')

# #bringing in the player values 
# player_values_df = pd.read_csv('https://raw.githubusercontent.com/dynastyprocess/data/master/files/values.csv')

# #filtering out the picks, getting rid of the mid early late pick values 
# player_values_df['position'] = player_values_df['pos'].astype(str)
# player_values_df = player_values_df[player_values_df['player'].str.contains('Early | Late | Mid ') == False]
# pick_values_df = player_values_df.loc[player_values_df['position'] =='PICK']
# pick = 'Pick'
# pick_values_df['Team'] = pick

# pick_values_df = pick_values_df[['player','position','Team','value_1qb','value_2qb']]
# #adding that wierd decimal thing 
# final_draft_order_df["pick_concat"] = final_draft_order_df.Pick.map("{:02}".format)

# #naming players to match dynasty process values 

# year = date.today().year
# this_year = str(year)
# next_year = str(year + 1)
# year_following = str(year + 2) 

# final_draft_order_df = final_draft_order_df.astype(str)
# #This function adds the appropriate suffix for each number 
# def pick_names(row):
#     if row['Year'] == next_year or row['Year'] == year_following:
#         if row['Round'] == '1':
#             return  row['Year'] + " " + row['Round'] + "st"
#         if row['Round'] == '2':
#             return  row['Year'] + " " + row['Round'] + "nd"
#         if row['Round'] == '3':
#             return  row['Year'] + " " + row['Round'] + "rd"
#         if row['Round'] == '4':
#             return  row['Year'] + " " + row['Round'] + "th"
#         if row['Round'] == '5':
#             return  row['Year'] + " " + row['Round'] + "th"
#     elif row['Year'] == this_year:
#         return row['Year'] + " " + "Pick" + " " + row['Round'] + "." + row['pick_concat']
        
# final_draft_order_df['player'] = final_draft_order_df.apply(lambda row: pick_names(row), axis=1)

# final_draft_order_df =final_draft_order_df[['roster_id','display_name','player']]

# from datetime import datetime

# pick_values_df = pd.merge(final_draft_order_df,pick_values_df, on='player', how='left')
# roster_values_df = roster_values_df[['display_name','player_id','full_name','position','team','value_1qb','value_2qb']]
# roster_values_df = roster_values_df.rename(columns={'full_name': 'Player','position':'Pos','display_name':'Manager', 'team': 'Team', 'value_1qb': 'DyPro 1QB', 'value_2qb':'DyPro 2QB' })
# pick_values_df = pick_values_df[['display_name', 'player','position','Team','value_1qb', 'value_2qb']]
# pick_values_df = pick_values_df.rename(columns={'display_name': 'Manager','position': 'Pos', 'player': 'Player','value_1qb': 'DyPro 1QB', 'value_2qb':'DyPro 2QB' })
# # print(pick_values_df.head())
# # print(roster_values_df)



# sleeper_rosters_dypro_df = pd.concat([pick_values_df,roster_values_df], ignore_index=True)
# sleeper_rosters_dypro_df.sort_values(by= ['DyPro 2QB'], inplace=True, ascending = False)

# # dypro_total_values_df = sleeper_rosters_dypro_df.groupby('Manager').agg({'DyPro 2QB': sum})

# # sleeper_rosters_dypro_df['DyPro 2Q']


# import plotly.express as px

# fig = px.histogram(sleeper_rosters_dypro_df, x="Manager", y="DyPro 2QB",  color='Pos', barmode='group', text_auto = True,
#              height=400)

# # fig.show()

# fig2 = px.histogram(sleeper_rosters_dypro_df, x="Manager", y="DyPro 2QB", text_auto=True,
#              height=400)

# import plotly.graph_objects as go
# from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

# st.title("Sleeper Dashboard")
# # add this
# gb = GridOptionsBuilder.from_dataframe(sleeper_rosters_dypro_df)
# gb.configure_pagination()
# gridOptions = gb.build()
# AgGrid(sleeper_rosters_dypro_df, gridOptions=gridOptions)

# st.plotly_chart(fig2, use_container_width=True)
# st.plotly_chart(fig, use_container_width=True)



# # ktc_df = pd.read_csv('https://raw.githubusercontent.com/Adeiko/AdeTrades/master/KtcValues.csv')
# # ktc_players = ktc_df.loc[ktc_df['Sleeper_ID'] > 0]
# # ktc_players = ktc_df.rename(columns={'Sleeper_ID':'player_id'})

# # dypro_players_ktc_df = sleeper_rosters_dypro_df.merge(ktc_plauers how = 'left', on='')

# # ktc_picks = ktc_df.loc[ktc_df['Sleeper_ID'].isnull()]
# # ktc_picks = ktc_picks[ktc_picks['Player_Name'].str.contains('2021') == False]

# # print(ktc_picks.head(50))



# # # pick_values_df.to_csv(f'/Users/nick/Desktop/FantasyDashboard/Sleeper/pick_values.csv', index = False)






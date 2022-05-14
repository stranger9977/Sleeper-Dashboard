# # -*- coding: utf-8 -*-
# """draft_dashboard1.ipynb
#
# Automatically generated by Colaboratory.
#
# Original file is located at
#     https://colab.research.google.com/drive/1hRwzsgQ4nbkxYNDWf1q4PrYy2HxXwntY
# """
#
# pip install sleeper-api-wrapper

from sleeper_wrapper import League
import pandas as pd

league = League(824128043063820288)

rosters = league.get_rosters()
users = league.get_users()

import requests

response = requests.get("https://api.sleeper.app/v1/draft/824128043810394112/picks")
print(response)

data = response.json()

print(type(data))

picks_df_raw = pd.DataFrame(data)
print(picks_df_raw)

picks_df_raw.info(verbose=True)

picks_df = picks_df_raw[['player_id', 'picked_by', 'round', 'draft_slot', 'pick_no']]

picks_df['draft_slot'] = picks_df.draft_slot.map("{:02}".format)

picks_df['Pick'] = picks_df['round'].astype(str) + "." + picks_df['draft_slot'].astype(str)
picks_df

users_df = pd.DataFrame(users)
users_df = users_df[['user_id', 'display_name']]

from sleeper_wrapper import Players

players = Players()
players = players.get_all_players()

players_df = pd.DataFrame(players)
players_df = players_df.transpose()

players_df.head()

players_df.columns

users_picks = picks_df.merge(users_df, left_on='picked_by', right_on='user_id', how="left")
users_picks

draft_results = users_picks.merge(players_df, left_on='player_id', right_index=True, how='left')

draft_results.columns

draft_results_df = draft_results[['player_id_x', 'display_name', 'full_name', 'Pick', 'pick_no']]
draft_results_df

# import data from KTC, ADP, ETR, and DP

df = pd.read_csv('https://raw.githubusercontent.com/dynastyprocess/data/master/files/values-players.csv')
# ids to merge player values with sleeper ids
id_df = pd.read_csv('https://raw.githubusercontent.com/dynastyprocess/data/master/files/db_playerids.csv')

# pick_values_df = pd.read_csv('https://raw.githubusercontent.com/dynastyprocess/data/master/files/values-picks.csv')


id_df = id_df[['fantasypros_id', 'sleeper_id']]
values_df = pd.merge(df, id_df, how='left', left_on=['fp_id'], right_on=['fantasypros_id'])

DyPro_df = values_df.loc[values_df['pos'].isin(['QB', 'RB', 'WR', 'TE'])]

ktc_df = pd.read_csv('https://raw.githubusercontent.com/Adeiko/AdeTrades/master/KtcValues.csv')
DyPro_df

ktc_df

draft_value_df = ktc_df.merge(DyPro_df, left_on=['Sleeper_ID'], right_on=['sleeper_id'], how='left')

draft_value_df = draft_value_df.dropna(subset=['Sleeper_ID'])

draft_value_df['KTC Rank'] = draft_value_df['Value'].rank(ascending=False)
draft_value_df.sort_values(by='Value', ascending=False).head(100)

draft_value_df['DyPro Rank'] = draft_value_df['value_2qb'].rank(ascending=False)
draft_value_df.sort_values(by='value_2qb', ascending=False).head(100)

draft_value_df = draft_value_df[['Sleeper_ID', 'Player_Name', 'age', 'pos', 'team', 'KTC Rank', 'DyPro Rank']]
draft_value_df

draft_value_df.info(verbose=True)

adp_df = pd.read_csv('/content/2022 Startup ADP - Sheet1.csv')
adp_df.info(verbose=True)

adp_df = adp_df[['Round', 'ADP', 'Player']]

draft_value_df = draft_value_df.merge(adp_df, left_on=['Player_Name'], right_on=['Player'], how='left')
draft_value_df.head()

draft_value_df.head(100)

etr_df = pd.read_csv('/content/ETR Dynasty Rankings.csv')
etr_df

draft_value_df = draft_value_df.merge(etr_df, left_on=['Player_Name'], right_on=['Player'], how='left')
draft_value_df['ETR Rank'] = draft_value_df['SF/TE Prem']
draft_value_df.info(verbose=True)

ranks = ['KTC Rank', 'ETR Rank', 'ADP', 'DyPro Rank']
draft_value_df['Avg rank'] = draft_value_df[ranks].mean(axis=1)
draft_value_df['StD Rank'] = draft_value_df[ranks].std(axis=1)

draft_value_df.info(verbose=True)

draft_results_df.info(verbose=True)

draft_results_df

draft_results_df[['player_id_x', 'pick_no']] = draft_results_df[['player_id_x', 'pick_no']].astype(float)

draft_value_df = draft_value_df[
    ['Sleeper_ID', 'Player_Name', 'age', 'pos', 'team', 'ADP', 'Avg rank', 'StD Rank', 'ETR Rank', 'KTC Rank',
     'DyPro Rank', 'Round', 'Notes']]
draft_result_value_df = draft_results_df.merge(draft_value_df, left_on='player_id_x', right_on='Sleeper_ID',
                                               how='outer')
draft_result_value_df

draft_result_value_df = draft_result_value_df.dropna(subset=['Sleeper_ID'])
draft_result_value_df.info(verbose=True)

draft_result_value_df['diff'] = draft_result_value_df['pick_no'] - draft_result_value_df['ADP']

final_df = draft_result_value_df.rename(
    columns={'display_name': 'drafted_by', 'full_name': 'draft_player', 'pick_no': 'actual'})
final_df = final_df[
    ['Player_Name', 'team', 'pos', 'age', 'ADP', 'actual', 'drafted_by', 'diff', 'Avg rank', 'StD Rank', 'ETR Rank',
     'KTC Rank', 'DyPro Rank', 'Round', 'Notes']].sort_values(by='Avg rank')
final_df = final_df[:300]

from sleeper_wrapper import League
from sleeper_wrapper import User
from sleeper_wrapper import Players
import pandas as pd
import streamlit as st
import requests
import plotly.express as px

st.set_page_config(page_title="Run_the_Sims")
user_input = st.text_input("enter your league id here", 824128043063820288)

league = League(user_input)
league_info = League.get_league(league)
response = requests.get(f"https://api.sleeper.app/v1/draft/{league_info['draft_id']}/picks")

league_name = str(league_info['name'])
st.header(league_name)
rosters = league.get_rosters()
users = league.get_users()
data = response.json()
picks_df_raw = pd.DataFrame(data)

picks_df = picks_df_raw[['player_id', 'picked_by', 'round', 'draft_slot', 'pick_no']]
picks_df['draft_slot'] = picks_df.draft_slot.map("{:02}".format)

picks_df['Pick'] = picks_df['round'].astype(str) + "." + picks_df['draft_slot'].astype(str)

users_df = pd.DataFrame(users)
users_df = users_df[['user_id', 'display_name']]

players_df = pd.read_csv('/Users/nick/Sleeper-Dashboard/Sleeper/players-2022-04-13.csv')

users_picks = picks_df.merge(users_df, left_on='picked_by', right_on='user_id', how="left")

draft_results = users_picks.merge(players_df, on='player_id', how='left')

draft_results_df = draft_results[['player_id', 'display_name', 'full_name', 'weight', 'height', 'Pick', 'pick_no']]

# import data from KTC, ADP, ETR, and DP

df = pd.read_csv('https://raw.githubusercontent.com/dynastyprocess/data/master/files/values-players.csv')
# ids to merge player values with sleeper ids
id_df = pd.read_csv('https://raw.githubusercontent.com/dynastyprocess/data/master/files/db_playerids.csv')

# pick_values_df = pd.read_csv('https://raw.githubusercontent.com/dynastyprocess/data/master/files/values-picks.csv')


id_df = id_df[['fantasypros_id', 'sleeper_id']]
values_df = pd.merge(df, id_df, how='left', left_on=['fp_id'], right_on=['fantasypros_id'])

DyPro_df = values_df.loc[values_df['pos'].isin(['QB', 'RB', 'WR', 'TE'])]

ktc_df = pd.read_csv('https://raw.githubusercontent.com/Adeiko/AdeTrades/master/KtcValues.csv')

draft_value_df = ktc_df.merge(DyPro_df, left_on=['Sleeper_ID'], right_on=['sleeper_id'], how='left')
draft_value_df = draft_value_df.dropna(subset=['Sleeper_ID'])

draft_value_df = draft_value_df.rename(columns={'Value': 'KTC Value', 'value_2qb': "DyPro Value"})

draft_value_df = draft_value_df[['Sleeper_ID', 'Player_Name', 'age', 'pos', 'team', 'KTC Value', 'DyPro Value']]

ranks = ['KTC Value', 'DyPro Value']
draft_value_df['Sims Value'] = draft_value_df[ranks].mean(axis=1).astype(int)
draft_results_df[['player_id', 'pick_no']] = draft_results_df[['player_id', 'pick_no']].astype(float)

draft_value_df = draft_value_df[['Sleeper_ID', 'Player_Name', 'age', 'pos', 'team', 'Sims Value']]
draft_result_value_df = draft_results_df.merge(draft_value_df, left_on='player_id', right_on='Sleeper_ID', how='outer')

final_df = draft_result_value_df.rename(columns={'display_name': 'Manager'})
final_df = final_df[['Player_Name', 'team', 'pos', 'age', 'pick_no', 'Manager', 'Sims Value','weight', 'height' ]].sort_values(
    by='pick_no')
final_df = final_df.dropna(subset=['pick_no'])
values = {"team": "ATL", "pos": 'WR', "age": 20.8}
final_df = final_df.fillna(value=values)
final_df

fig = px.histogram(final_df, x="Manager", y="Sims Value", color='pos', barmode='group', text_auto=True,
                   height=400, title='Value by Position')
fig2 = px.histogram(final_df, x="Manager", y="Sims Value", text_auto=True,
                    height=400, title='Total Value')

fig3 = px.histogram(final_df, x='Manager', y='age', text_auto=True, title='Total Team Age')

fig4 = px.histogram(final_df, x='Manager', y='weight', text_auto=True, title='Value by THICCness')
fig5 = px.histogram(final_df, x='Manager', y='height', text_auto=True, title='Who drafts the short kings?')
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)
st.plotly_chart(fig4, use_container_width=True)
st.plotly_chart(fig5, use_container_width=True)

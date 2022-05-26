import pandas as pd
import plotly.express as px
import requests
from sleeper_wrapper import League
import streamlit as st
import plotly.graph_objects as go


# Page setting
st.set_page_config(page_title="Sleeper Data Science Dashboard", layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

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

players_df = pd.read_csv(
    'https://raw.githubusercontent.com/stranger9977/Sleeper-Dashboard/main/Data/players-2022-04-13.csv')

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

values_for_graphs = draft_value_df[['Sleeper_ID', 'Player_Name', 'age', 'pos', 'team', 'Sims Value']]
print(values_for_graphs.info(verbose=True))
# values_for_graphs
# draft_results_df[['player_id', 'pick_no']] = draft_results_df[['player_id', 'pick_no']].astype(float)

draft_value_df['KTC Rank'] = draft_value_df['KTC Value'].rank(ascending=False)
draft_value_df.sort_values(by='KTC Value', ascending=False).head(100)

draft_value_df['DyPro Rank'] = draft_value_df['DyPro Value'].rank(ascending=False)
draft_value_df.sort_values(by='DyPro Value', ascending=False).head(100)

draft_ranks_df = draft_value_df[['Sleeper_ID', 'Player_Name', 'age', 'pos', 'team', 'KTC Rank', 'DyPro Rank']]

adp_df = pd.read_csv(
    'https://raw.githubusercontent.com/stranger9977/Sleeper-Dashboard/sleeper-app/Data/2022%20Startup%20ADP%20-%20Sheet1.csv')

adp_df = adp_df[['Round', 'ADP', 'Player']]

draft_value_df = draft_value_df.merge(adp_df, left_on=['Player_Name'], right_on=['Player'], how='left')

etr_df = pd.read_csv(
    'https://raw.githubusercontent.com/stranger9977/Sleeper-Dashboard/sleeper-app/Data/ETR%20Dynasty%20Rankings%20May.csv')

draft_value_df = draft_value_df.merge(etr_df, left_on=['Player_Name'], right_on=['Player'], how='left')
draft_value_df['ETR Rank'] = draft_value_df['SF/TE Prem']

ranks = ['KTC Rank', 'ETR Rank', 'ADP', 'DyPro Rank']
draft_value_df['Sims Rank'] = draft_value_df[ranks].mean(axis=1)
positions = ['QB', 'RB', 'WR', 'TE']
position_filter = draft_results_df['position'].isin(positions)
draft_results_df = draft_results_df[position_filter]
draft_results_df[['player_id', 'pick_no']] = draft_results_df[['player_id', 'pick_no']].astype(float)

draft_value_df = draft_value_df[
    ['Sleeper_ID', 'Player_Name', 'age', 'pos', 'team', 'ADP', 'Sims Rank']]
draft_result_value_df = draft_results_df.merge(draft_value_df, left_on='player_id', right_on='Sleeper_ID',
                                               how='outer')

values_for_graphs = draft_results_df.merge(values_for_graphs, left_on='player_id', right_on='Sleeper_ID',
                                           how='left')

values_for_graphs = values_for_graphs.dropna(subset=['pick_no'])
print(values_for_graphs.info(verbose=True))
remaining_players = draft_result_value_df.dropna(subset=['Sleeper_ID'])
draft_result_value_df = draft_result_value_df.dropna(subset=['pick_no'])
draft_result_value_df = draft_result_value_df.rename(
    columns={'display_name': 'Manager', 'full_name': 'Player', 'pick_no': 'Draft Pick', })
draft_result_value_df = draft_result_value_df[
    [ 'Manager', 'Player', 'team', 'pos', 'age', 'ADP', 'Draft Pick','Sims Rank']].sort_values(by='Draft Pick')

draft_result_value_df['EV'] = draft_result_value_df['Draft Pick'] - draft_result_value_df['Sims Rank']
draft_result_value_df['Draft Pick'] = draft_result_value_df['Draft Pick'].astype(int)

draft_result_value_df = draft_result_value_df[:300]

values = {"team": "ATL", "pos": 'WR', "age": 20.8}
draft_result_value_df = draft_result_value_df.fillna(value=values)
values_for_graphs = values_for_graphs.fillna(value=values)
draft_result_value_df
value_graph = values_for_graphs.sort_values(by=['Sims Value'], ascending=False)
top_5_best_picks = draft_result_value_df.sort_values(by=['EV'], ascending=False)[:5]
top_5_worst_picks = draft_result_value_df.sort_values(by=['EV'])[:5]



fig = px.histogram(values_for_graphs, x="display_name", y="Sims Value", color='pos', barmode='group', text_auto=True,
                   height=400, title='Value by Position')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig2 = px.histogram(values_for_graphs, x="display_name", y="Sims Value", text_auto=True,
                    height=400, title='Total Value')




st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig, use_container_width=True)


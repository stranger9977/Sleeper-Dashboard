import pandas as pd

underdog_df = pd.read_csv('/Users/nick/UnderdogVORmodel/data/Underdogdata/underdogadp_may.csv')
expert_df = pd.read_csv('/Users/nick/UnderdogVORmodel/data/fantasypros_projections.csv')

underdog_df['lastName'] = underdog_df['lastName'].str.split(' ').str[0]
underdog_df['Player'] = underdog_df['firstName'] + " " + underdog_df['lastName']
underdog_df['Player'] = underdog_df['Player'].str.replace(r'( [A-Z]*)$', '').str.strip().str.replace('-',
                                                                                                     '').str.replace(
    r'\bJr.$', '', regex=True).str.replace(r'\bSr.$', '', regex=True).str.replace('.', "").str.replace(r'\bII$', '',
                                                                                                       regex=True).str.replace(
    r'\bI$', '', regex=True).str.replace(r'\bIII$', '', regex=True).str.replace(r'\bIV$', '', regex=True).str.replace(
    r'\bV$', '', regex=True).str.strip()
expert_df['Player'] = expert_df['Player'].str.replace(r'( [A-Z]*)$', '').str.strip().str.replace('-', '').str.replace(
    r'\bJr.$', '', regex=True).str.replace(r'\bSr.$', '', regex=True).str.replace('.', "").str.replace(r'\bII$', '',
                                                                                                       regex=True).str.replace(
    r'\bI$', '', regex=True).str.replace(r'\bIII$', '', regex=True).str.replace(r'\bIV$', '', regex=True).str.replace(
    r'\bV$', '', regex=True).str.strip()

underdog_df = underdog_df[:344]

underdog_df = underdog_df[['id', 'Player', 'slotName', 'teamName', 'projectedPoints', 'adp', ]]

underdog_df[['adp', 'projectedPoints']] = underdog_df[['adp', 'projectedPoints']].astype(float)
expert_df['FPTS'] = expert_df['FPTS'].astype(float)
final_df = underdog_df.merge(expert_df, on="Player", how="left")

final_df['SimsProj'] = final_df[['FPTS', 'projectedPoints']].mean(axis='columns')

vor_df = final_df[['id', 'Player', 'slotName', 'teamName', 'adp', 'SimsProj']]
vor_df = vor_df.sort_values(by='adp')
# print(vor_df)

adp_df_cutoff = vor_df[:100]
replacement_players = {
    "RB": " ",
    "QB": " ",
    "WR": " ",
    "TE": " "
}

for __, row in adp_df_cutoff.iterrows():

    position = row['slotName']
    player = row['Player']

    if position in replacement_players:
        replacement_players[position] = player

vor_df = vor_df[['id', 'Player', 'slotName', 'teamName', 'SimsProj', 'adp']]
# print(replacement_players)

replacement_values = {}

for position, player_name in replacement_players.items():
    player = vor_df.loc[vor_df['Player'] == player_name]

    replacement_values[position] = player['SimsProj'].tolist()[0]

vor_df['VOR'] = vor_df.apply(
    lambda row: row['SimsProj'] - replacement_values.get(row['slotName']), axis=1
)

vor_df['VOR'] = vor_df['VOR'].apply(lambda x: (x - vor_df['VOR'].mean()) / vor_df['VOR'].std())

vor_df['VOR Rank'] = vor_df['VOR'].rank(ascending=False)
vor_df = vor_df.sort_values(by='VOR Rank', ascending=False)

num_teams = 12
num_spots = 18
draft_pool = num_teams * num_spots

vor_df['VOR Rank'] = vor_df['VOR Rank'].astype(float)

vor_df['Diff'] = vor_df['VOR Rank'] - vor_df['adp']


vor_df = vor_df.sort_values(by='VOR Rank', ascending=True)


vor_df.to_csv("/Users/nick/UnderdogVORmodel/vor_may.csv", index=False)
#
# print(df.head())
#
# #

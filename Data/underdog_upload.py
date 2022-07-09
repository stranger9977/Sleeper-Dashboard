import pandas as pd
# import nfl_data_py as nfl
pd.options.display.max_rows = 999
pd.options.display.max_columns = 999
machine_learning_projections = pd.read_csv('/Users/nick/Sleeper-Dashboard/Data/flex_0_5PPR copy.csv')
qb_ml = pd.read_csv('/Users/nick/Sleeper-Dashboard/Data/qb_4pt.csv')
paulsen_projections_df = pd.read_csv('/Users/nick/UnderdogVORmodel/data/4for4/4for4_projections_061922.csv')
etr_df = pd.read_csv('/Users/nick/Sleeper-Dashboard/Data/etr_underdog_rankings-2022-07-07.csv')
underdog_df = pd.read_csv('/Users/nick/Sleeper-Dashboard/Data/underdog_adp-2022-07-08.csv')

expert_df = pd.read_csv('/Users/nick/Sleeper-Dashboard/Data/expert_consensus_projections-2022-07-07.csv')

# underdog_df['lastName'] = underdog_df['lastName'].str.split(' ').str[0]
underdog_df['Player'] = underdog_df['firstName'] + " " + underdog_df['lastName']



underdog_df['Player'] = underdog_df['Player'].str.replace(r'( [A-Z]*)$', '').str.strip().str.replace('-',
                                                                                                     '').str.replace(
    r'\bJr.$', '', regex=True).str.replace(r'\bSr.$', '', regex=True).str.replace('.', "").str.replace(r'\bII$', '',
                                                                                                       regex=True).str.replace(
    r'\bI$', '', regex=True).str.replace(r'\bIII$', '', regex=True).str.replace(r'\bIV$', '', regex=True).str.replace(
    r'\bV$', '', regex=True).str.strip()
underdog_df['Player'] = underdog_df['Player'].replace()
expert_df['Player'] = expert_df['Player'].str.replace(r'( [A-Z]*)$', '').str.strip().str.replace('-', '').str.replace(
    r'\bJr.$', '', regex=True).str.replace(r'\bSr.$', '', regex=True).str.replace('.', "").str.replace(r'\bII$', '',
                                                                                                       regex=True).str.replace(
    r'\bI$', '', regex=True).str.replace(r'\bIII$', '', regex=True).str.replace(r'\bIV$', '', regex=True).str.replace(
    r'\bV$', '', regex=True).str.strip()

# paulsen_rankings_df['Player'] = paulsen_rankings_df['Player'].str.replace(r'( [A-Z]*)$', '').str.strip().str.replace(
#     '-', '').str.replace(
#     r'\bJr.$', '', regex=True).str.replace(r'\bSr.$', '', regex=True).str.replace('.', "").str.replace(r'\bII$', '',
#                                                                                                        regex=True).str.replace(
#     r'\bI$', '', regex=True).str.replace(r'\bIII$', '', regex=True).str.replace(r'\bIV$', '', regex=True).str.replace(
#     r'\bV$', '', regex=True).str.strip()

paulsen_projections_df['Player'] = paulsen_projections_df['Player'].str.replace(r'( [A-Z]*)$',
                                                                                '').str.strip().str.replace('-',
                                                                                                            '').str.replace(
    r'\bJr.$', '', regex=True).str.replace(r'\bSr.$', '', regex=True).str.replace('.', "").str.replace(r'\bII$', '',
                                                                                                       regex=True).str.replace(
    r'\bI$', '', regex=True).str.replace(r'\bIII$', '', regex=True).str.replace(r'\bIV$', '', regex=True).str.replace(
    r'\bV$', '', regex=True).str.strip()

etr_df['Player'] = etr_df['Player'].str.replace(r'( [A-Z]*)$', '').str.strip().str.replace('-', '').str.replace(
    r'\bJr.$', '', regex=True).str.replace(r'\bSr.$', '', regex=True).str.replace('.', "").str.replace(r'\bII$', '',
                                                                                                       regex=True).str.replace(
    r'\bI$', '', regex=True).str.replace(r'\bIII$', '', regex=True).str.replace(r'\bIV$', '', regex=True).str.replace(
    r'\bV$', '', regex=True).str.strip()


#
#
machine_learning_projections = machine_learning_projections.append(qb_ml)
machine_learning_projections = machine_learning_projections.groupby('Player').sum().reset_index()

# print(machine_learning_projections.sort_values(by='Projection', ascending=False))
machine_learning_projections['Player'] = machine_learning_projections['Player'].str.replace(r'( [A-Z]*)$', '').str.strip().str.replace('-', '').str.replace(
    r'\bJr.$', '', regex=True).str.replace(r'\bSr.$', '', regex=True).str.replace('.', "").str.replace(r'\bII$', '',
                                                                                                       regex=True).str.replace(
    r'\bI$', '', regex=True).str.replace(r'\bIII$', '', regex=True).str.replace(r'\bIV$', '', regex=True).str.replace(
    r'\bV$', '', regex=True).str.strip()
# underdog_adp['Player'] = underdog_adp['Player'].str.replace(r'( [A-Z]*)$', '').str.strip().str.replace('-', '').str.replace(
#     r'\bJr.$', '', regex=True).str.replace(r'\bSr.$', '', regex=True).str.replace('.', "").str.replace(r'\bII$', '',
#                                                                                                        regex=True).str.replace(
#     r'\bI$', '', regex=True).str.replace(r'\bIII$', '', regex=True).str.replace(r'\bIV$', '', regex=True).str.replace(
#     r'\bV$', '', regex=True).str.strip()


# print(machine_learning_projections)
# paulsen_df = paulsen_rankings_df.merge(paulsen_projections_df, on="Player", how="left")
paulsen_df = underdog_df.merge(paulsen_projections_df, on="Player", how="left")
# paulsen_df = paulsen_df.merge(etr_df, on="Player", how="left")
print(paulsen_df[paulsen_df['ADP'].isnull()])
underdog_df = underdog_df[:344]
#
underdog_df = underdog_df[['id', 'Player', 'slotName', 'teamName', 'projectedPoints', 'adp', ]]
machine_learning_projections['Projection'] = machine_learning_projections['Projection'].astype(float)
paulsen_df['FF Pts'] = paulsen_df['FF Pts'].astype(float)
underdog_df[['adp', 'projectedPoints']] = underdog_df[['adp', 'projectedPoints']].astype(float)
expert_df['FPTS'] = expert_df['FPTS'].astype(float)
#
# final_df = underdog_df.merge(expert_df, on="Player", how="left")
final_df = paulsen_df.merge(expert_df, on='Player', how="left")
final_df = final_df.merge(machine_learning_projections, on='Player', how='left')
etr_df.rename(columns={'Team':'etr_TEAM', 'id':'ETR_id'}, inplace=True)
final_df = final_df.merge(etr_df, on='Player', how='left')
etr_df.rename(columns={'Team':'etr_TEAM', 'id':'ETR_id'}, inplace=True)
print(final_df.columns)

projections = ['FPTS', 'projectedPoints', 'FF Pts','Projection']

final_df['teamName']=final_df['teamName'].fillna('Free Agent')

final_df['adp'] = final_df['adp'].replace("-",216.0).astype(float)
final_df.sort_values(by = ['slotName', 'slotName'], ascending = [False, True], inplace=True)
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
numerics = final_df.select_dtypes(include=numerics)
numerics = ['adp', 'projectedPoints', 'byeWeek', 'FF Pts', 'ADP', 'Pass Comp',
       'Pass Att', 'Pass Yds', 'Pass TD', 'INT', 'Rush Att', 'Rush Yds',
       'Rush TD', 'Rec_x', 'Rec Yds', 'Rec TD', 'BYE', 'Pa1D', 'Ru1D', 'Rec1D',
       'Fum', 'XP', 'FG', 'PassAtt', 'Cmp', 'PassYds', 'PassTds', 'PassInts',
       'RushAtt', 'RushYds', 'RushTds', 'FL', 'FPTS', 'Rec_y', 'RecYds',
       'RecTds', 'Projection', 'ETR Rank', 'Underdog ADP', 'ADP Differential']
final_df[numerics] = round(final_df[numerics],1)

for numeric in numerics:
    final_df[numeric].interpolate(method='linear',axis=0, inplace=True)
final_df['SimsProj'] = round(final_df[['FPTS', 'projectedPoints', 'FF Pts','Projection']].mean(axis='columns'),2)

projections_df = final_df
projections_df.to_csv('/Users/nick/Sleeper-Dashboard/Data/projections.csv', index=False)
print(final_df.columns)

vor_df = final_df
vor_df = vor_df.sort_values(by='adp')
print(vor_df.columns)
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

vor_df = round( vor_df[['id', 'Player', 'slotName', 'teamName','ETR Rank', 'adp','SimsProj', 'FPTS', 'projectedPoints', 'FF Pts','Projection']], 2)
print(vor_df.info(verbose=True))
#
#
# print(replacement_players)
#
replacement_values = {}
#
# for position, player_name in replacement_players.items():
#     player = vor_df.loc[vor_df['Player'] == player_name]
#
#     replacement_values[position] = player['SimsProj'].tolist()[0]
#
# vor_df['VOR'] = vor_df.apply(
#     lambda row: row['SimsProj'] - replacement_values.get(row['slotName']), axis=1
# )
#
# vor_df['VOR'] = vor_df['VOR'].apply(lambda x: (x - vor_df['VOR'].mean()) / vor_df['VOR'].std())
#
# vor_df['VOR Rank'] = vor_df['VOR'].rank(ascending=False)

adp_df_cutoff = vor_df[:120]
print(adp_df_cutoff)
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

vor_df = round( vor_df[['id', 'Player', 'slotName', 'teamName','ETR Rank', 'adp','SimsProj', 'FPTS', 'projectedPoints', 'FF Pts','Projection']], 2)
print(vor_df.info(verbose=True))
#
#
print(replacement_players)

projection = projections

for projection in projections:
    for position, player_name in replacement_players.items():
            player = vor_df.loc[vor_df["Player"] == player_name]
            replacement_values[position] = player[projection].tolist()[0]

    vor_df[projection + 'VOR']=vor_df.apply(
            lambda row: row[projection] - replacement_values.get(row['slotName']), axis=1)
    vor_df[projection + "VOR"] = vor_df[projection].apply(lambda x: (x - vor_df[projection].mean()) / vor_df[projection].std())

vor = ['FPTSVOR','projectedPointsVOR','FF PtsVOR', 'ProjectionVOR']

for vor in vor:
        vor_df[vor + "_Rank" ]= vor_df[vor].rank(ascending=False)
else:
        vor_df[vor + "_Rank"] = vor_df[vor].rank(ascending=False)


vor_df.loc[vor_df['slotName'] == "QB","SimsRank"] = vor_df['adp']

for __, row in vor_df.iterrows():

    position = row['slotName']
    ranking = row['SimsRank']

    if position =='QB':
        ranking =row['ETR Rank']



columns = projections



vor_df['VOR Rank'] = round(vor_df[['FF PtsVOR_Rank','FPTSVOR_Rank','ProjectionVOR_Rank','projectedPointsVOR_Rank']].mean(axis='columns'),1)
vor_df['VOR Rank'] = vor_df['VOR Rank'].astype(float)
vor_df['SimsMedian'] = round(vor_df[['ETR Rank','adp','VOR Rank']].median(axis='columns'),1)
vor_df['SimsRank'] = vor_df['SimsMedian'].rank(ascending=True)
# vor_df['SimsRank'] = vor_df[['SimsRank', 'adp']].mean(axis='columns')
vor_df['Diff'] = round(vor_df['adp'] - vor_df['SimsRank'],1)
vor_df = vor_df.sort_values(by='SimsRank')
vor_df.rename(columns={"FF PtsVOR_Rank": '4for4 Rank', 'projectedPointsVOR_Rank':"Underdog Rank", 'FPTSVOR_Rank': "ECR Rank", 'ProjectionVOR_Rank':"ML Rank"}, inplace=True)
vor_df = vor_df[['id', 'Player', 'slotName', 'teamName','SimsMedian', 'SimsRank','adp','Diff','ETR Rank', 'VOR Rank',
       'ECR Rank', 'Underdog Rank', '4for4 Rank', 'ML Rank']]

#
vor_df.to_csv("/Users/nick/Sleeper-Dashboard/Data/vor_july.csv", index=False)
# #
#
# #
# # #

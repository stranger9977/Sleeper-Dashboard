
import pandas as pd
import numpy as np
from datetime import datetime
pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

#importing most up to date rankings, adp, and projections
now = datetime.now()
year = now.strftime("%Y")[2:]
month = now.strftime("%m")
day = now.strftime("%d")
machine_learning_projections = pd.read_csv('/Users/nick/Sleeper-Dashboard/Data/flex_0_5PPR copy.csv')
qb_ml = pd.read_csv('/Users/nick/Sleeper-Dashboard/Data/qb_4pt.csv')
paulsen_projections_df = pd.read_csv(f'/Users/nick/Sleeper-Dashboard/Data/4for4_projections_{month + day + year}.csv')
etr_df = pd.read_csv(f'/Users/nick/Sleeper-Dashboard/Data/etr_underdog_rankings-{datetime.now():%Y-%m-%d}.csv')
underdog_df = pd.read_csv(f'/Users/nick/Sleeper-Dashboard/Data/underdog_adp-{datetime.now():%Y-%m-%d}.csv')
expert_df = pd.read_csv(f'/Users/nick/Sleeper-Dashboard/Data/expert_consensus_projections-{datetime.now():%Y-%m-%d}.csv')
underdog_df['Player'] = underdog_df['firstName'] + " " + underdog_df['lastName']
underdog_df = underdog_df.loc[underdog_df['adp'] != '-']

#Name Cleaning
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
underdog_df['Player'] = underdog_df['Player'].str.replace(r'( [A-Z]*)$', '').str.strip().str.replace('-',
                                                                                                     '').str.replace(
    r'\bJr.$', '', regex=True).str.replace(r'\bSr.$', '', regex=True).str.replace('.', "").str.replace(r'\bII$', '',
                                                                                                       regex=True).str.replace(
    r'\bI$', '', regex=True).str.replace(r'\bIII$', '', regex=True).str.replace(r'\bIV$', '', regex=True).str.replace(
    r'\bV$', '', regex=True).str.strip()
expert_df['Player'] = expert_df['Player'].str.replace(r'( [A-Z]*)$', '').str.strip().str.replace('-', '').str.replace(
    r'\bJr.$', '', regex=True).str.replace(r'\bSr.$', '', regex=True).str.replace('.', "").str.replace(r'\bII$', '',
                                                                                                       regex=True).str.replace(
    r'\bI$', '',)

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

etr_df = etr_df.replace({'Player': {"Kenneth Walker": "Ken Walker", "Devonta Smith": "DeVonta Smith","Mitchell Trubisky":"Mitch Trubisky"}})
underdog_df = underdog_df.replace({'Player': {"Joshua Palmer": "Josh Palmer", "William Fuller":"Will Fuller", "Mitchell Trubisky":"Mitch Trubisky","Robby Anderson":"Robbie Anderson"}})
paulsen_projections_df_df = paulsen_projections_df.replace({'Player': {"Joshua Palmer": "Josh Palmer"}})
expert_df = expert_df.replace({'Player': {"Joshua Palmer": "Josh Palmer", "William Fuller":"Will Fuller", "Mitchell Trubisky":"Mitch Trubisky","Robby Anderson":"Robbie Anderson", "Amon-Ra St.":"Amon-Ra St. Brown"}})
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
#
#
# print(machine_learning_projections)
# paulsen_df = paulsen_rankings_df.merge(paulsen_projections_df, on="Player", how="left")

#merging data
paulsen_df = underdog_df.merge(paulsen_projections_df, on="Player", how="left")
# paulsen_df = paulsen_df.merge(etr_df, on="Player", how="left")
underdog_df = underdog_df[:344]


underdog_df = underdog_df[['id', 'Player', 'slotName', 'teamName', 'projectedPoints', 'adp', ]]
machine_learning_projections['Projection'] = machine_learning_projections['Projection'].astype(float)
paulsen_df['FF Pts'] = paulsen_df['FF Pts'].astype(float)
underdog_df[['adp', 'projectedPoints']] = underdog_df[['adp', 'projectedPoints']].astype(float)
expert_df['FPTS'] = expert_df['FPTS'].astype(float)
#
# final_df = underdog_df.merge(expert_df, on="Player", how="left")
final_df = paulsen_df.merge(expert_df, on='Player', how="left")
final_df = final_df.merge(machine_learning_projections, on='Player', how='left')
etr_df.rename(columns={'Team':'etr_TEAM', 'id':'id'}, inplace=True)
final_df = final_df.merge(etr_df, on=['id','Player'] , how='left')
etr_df.rename(columns={'Team':'etr_TEAM', 'id':'ETR_id'}, inplace=True)
final_df.drop(columns=['lineupStatus','byeWeek'],inplace=True)
final_df.dropna(inplace=True)

projections = ['FPTS', 'projectedPoints', 'FF Pts','Projection']

final_df['teamName']=final_df['teamName'].fillna('Free Agent')

final_df['adp'] = final_df['adp'].replace("-",216.0).astype(float)
# print(final_df.columns)
final_df.sort_values(by = ['ETR Pos Rank'], inplace=True)
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
numerics = final_df.select_dtypes(include=numerics)
numerics = ['adp', 'projectedPoints', 'FF Pts', 'ADP', 'Pass Comp',
       'Pass Att', 'Pass Yds', 'Pass TD', 'INT', 'Rush Att', 'Rush Yds',
       'Rush TD', 'Rec_x', 'Rec Yds', 'Rec TD', 'BYE', 'Pa1D', 'Ru1D', 'Rec1D',
       'Fum', 'XP', 'FG', 'PassAtt', 'Cmp', 'PassYds', 'PassTds', 'PassInts',
       'RushAtt', 'RushYds', 'RushTds', 'FL', 'FPTS', 'Rec_y', 'RecYds',
       'RecTds', 'Projection', 'ETR Rank', 'Underdog ADP', 'ADP Differential']
final_df[numerics] = round(final_df[numerics],1)
# for numeric in numerics:
#     final_df[numeric].interpolate(method='linear',axis=0, inplace=True)
final_df['SimsProj'] = round(final_df[['FPTS', 'FF Pts']].mean(axis='columns'),2)
# qb_df = final_df[final_df['slotName'] == "QB"]
#
# final_df = final_df[final_df['slotName'] != "QB"]



vor_df = final_df
vor_df = vor_df.sort_values(by='adp')
projections_df = vor_df


vor_df['ADP RANK'] = vor_df['adp'].rank()
vor_df.sort_values(by='ADP RANK', inplace=True)
projections_df.to_csv('/Users/nick/Sleeper-Dashboard/Data/projections.csv', index=False)
adp_df_cutoff = vor_df[:96]
replacement_players = {
    "QB": " ",
    "RB": " ",
    "WR": " ",
    "TE": " "
}

for __, row in adp_df_cutoff.iterrows():

    position = row['slotName']
    player = row['Player']

    if position in replacement_players:
        replacement_players[position] = player

vor_df = round( vor_df[['id', 'Player', 'slotName', 'teamName','ETR Rank', 'adp','SimsProj', 'FPTS','FF Pts']], 2)
#
#
# print(replacement_players)
#
replacement_values = {}
#
for position, player_name in replacement_players.items():
    player = vor_df.loc[vor_df['Player'] == player_name]

    replacement_values[position] = player['SimsProj'].tolist()[0]

vor_df['VOR'] = vor_df.apply(
    lambda row: row['SimsProj'] - replacement_values.get(row['slotName']), axis=1)

vor_df['VOR'] = vor_df['VOR'].apply(lambda x: (x - vor_df['VOR'].mean()) / vor_df['VOR'].std())

vor_df['VOR Rank'] = vor_df['VOR'].rank(ascending=False)
# print(vor_df[['Player','VOR Rank']])

vor_df = round( vor_df[['id', 'Player', 'slotName', 'teamName','ETR Rank', 'adp','SimsProj', 'FPTS', 'FF Pts','VOR Rank']], 2)

#
#
print(replacement_players)
print(replacement_values)
# projection = projections
#
# for projection in projections:
#     for position, player_name in replacement_players.items():
#             player = vor_df.loc[vor_df["Player"] == player_name]
#             print(replacement_values)
#             replacement_values[position] = player[projection].tolist()[0]
#
#     vor_df[projection + 'VOR']=vor_df.apply(
#             lambda row: row[projection] - replacement_values.get(row['slotName']), axis=1)
#     vor_df[projection + "VOR"] = vor_df[projection].apply(lambda x: (x - vor_df[projection].mean()) / vor_df[projection].std())
#


# vor = ['FPTSVOR','projectedPointsVOR','FF PtsVOR', 'ProjectionVOR']
#
# for vor in vor:
#         vor_df[vor + "_Rank" ]= vor_df[vor].rank(ascending=False)


# vor_df.loc[vor_df['slotName'] == "QB","SimsRank"] = vor_df['adp']



# qb_df['SimsRank'] = round(qb_df[['ETR Rank','adp']].mean(axis='columns'),1)
# qb_df['ECR Rank'] = np.nan
# qb_df['4for4 Rank'] = np.nan
# qb_df['Diff'] = round(qb_df['adp'] - qb_df['SimsRank'],1)
# qb_df = qb_df[['id', 'Player', 'slotName', 'teamName', 'SimsRank','adp','Diff','ETR Rank',
#        'ECR Rank', '4for4 Rank']]
# vor_df['VOR Rank'] = round(vor_df[['FF PtsVOR_Rank','FPTSVOR_Rank','ProjectionVOR_Rank','projectedPointsVOR_Rank']].mean(axis='columns'),1)
# vor_df['VOR Rank'] = vor_df['VOR Rank'].astype(float)
# vor_df['SimsAVG'] = round(vor_df[['FF PtsVOR_Rank','FPTSVOR_Rank']].mean(axis='columns'),1)
# vor_df['SimsAVG'] = round(vor_df[['ETR Rank','VOR RANK']].mean(axis='columns'),1)
# vor_df['SimsAVG'] = round(vor_df[['adp','SimsAVG']].mean(axis='columns'),1)
# vor_df['SimsRank'] = vor_df['SimsAVG'].rank(ascending=True)
vor_df['SimsRank'] = round(vor_df[['ETR Rank','adp','VOR Rank']].mean(axis='columns'),1)
#adjusting qbs scores by 18 to align with adp better.

# vor_df[vor_df['slotName']=='QB']['SimsAVG'] = vor_df['SimsAVG'] + 18
# vor_df['SimsRank'] = vor_df['SimsAVG'].rank(ascending=True)

# qbs['SimsAVGFixed'] = (qbs['SimsAVG']  + 18)

# vor_df = vor_df.merge(qbs, how='left')


vor_df['SD']= round(vor_df[['ETR Rank','VOR Rank','adp']].std(axis='columns'),2)
vor_df['Diff'] = round(vor_df['adp'] - vor_df['SimsRank'],1)
# vor_df.rename(columns={"FF PtsVOR_Rank": '4for4 Rank', 'projectedPointsVOR_Rank':"Underdog Rank", 'FPTSVOR_Rank': "ECR Rank", 'ProjectionVOR_Rank':"ML Rank"}, inplace=True)
vor_df = vor_df[['id', 'Player', 'slotName', 'teamName', 'SimsRank','adp','Diff','ETR Rank','VOR Rank','SD']]

# vor_df = pd.concat([vor_df,qb_df])

vor_df = vor_df.sort_values(by='SimsRank')
vor_df.isnull()
vor_df.to_csv("/Users/nick/Sleeper-Dashboard/Data/vor_july.csv", index=False)
# #
#
# #
# # #

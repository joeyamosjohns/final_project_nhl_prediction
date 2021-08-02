import pandas as pd
import numpy as np


##import all the files 

##file paths

Kaggle_path = "/Users/joejohns/data_bootcamp/Final_Project_NHL_prediction/Data/Kaggle_Data_Ellis/"
mp_path = "/Users/joejohns/data_bootcamp/Final_Project_NHL_prediction/Data/Money_Puck_Data/"
betting_path = "/Users/joejohns/data_bootcamp/Final_Project_NHL_prediction/Data/Betting_Data/"

##Kaggle files

df_game = pd.read_csv(Kaggle_path+'game.csv')
df_game_team_stats = pd.read_csv(Kaggle_path+'game_teams_stats.csv')
df_game_skater_stats = pd.read_csv(Kaggle_path+'game_skater_stats.csv')
df_game_goalie_stats = pd.read_csv(Kaggle_path+'game_goalie_stats.csv')

##more subtle Kaggle features:
df_game_scratches = pd.read_csv(Kaggle_path+'game_scratches.csv')
df_game_officials = pd.read_csv(Kaggle_path+'game_officials.csv')
df_team_info = pd.read_csv(Kaggle_path+'team_info.csv')

## grab all the moneypuck data 

df_mp_teams = pd.read_csv(mp_path+'all_teams.csv')


## grab all betting data 
df1 = pd.read_excel(io = betting_path+'nhl odds 2007-08.xlsx')
df2 = pd.read_excel(io = betting_path+'nhl odds 2008-09.xlsx')
df3 = pd.read_excel(io = betting_path+'nhl odds 2009-10.xlsx')
df4 = pd.read_excel(io = betting_path+'nhl odds 2010-11.xlsx')
df5 = pd.read_excel(io = betting_path+'nhl odds 2011-12.xlsx')
df6 = pd.read_excel(io = betting_path+'nhl odds 2012-13.xlsx')
df7 = pd.read_excel(io = betting_path+'nhl odds 2013-14.xlsx')
df8 = pd.read_excel(io = betting_path+'nhl odds 2014-15.xlsx')
df9 = pd.read_excel(io = betting_path+'nhl odds 2015-16.xlsx')
df10 = pd.read_excel(io = betting_path+'nhl odds 2016-17.xlsx')
df11 = pd.read_excel(io = betting_path+'nhl odds 2017-18.xlsx')
df12 = pd.read_excel(io = betting_path+'nhl odds 2018-19.xlsx')
df13 = pd.read_excel(io = betting_path+'nhl odds 2019-20.xlsx')


###add missing season to betting files (important)

df1['season'] = 20072008
df2['season'] = 20082009
df3['season'] = 20092010
df4['season'] = 20102011
df5['season'] = 20112012
df6['season'] = 20122013
df7['season'] = 20132014
df8['season'] = 20142015
df9['season'] = 20152016
df10['season'] = 20162017
df11['season'] = 20172018
df12['season'] = 20182019
df13['season'] = 20192020

df_betting = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13])

##### restrict data sets 


df_betting = df_betting.loc[:, ['Date', 'season','VH', 'Team', 'Open']].copy()
df_mp_teams_all = df_mp_teams.loc[df_mp_teams['situation'] == 'all', :].copy()

##drop duplicates and one column had some NaN

df_game.drop_duplicates(inplace = True)
df_game.drop(columns = ['home_rink_side_start'], inplace = True)

##used the following function to check NaN 

data_frames = [df_mp_teams,
df_mp_teams_all,
df_betting,
df_game,
df_game_team_stats, 
df_game_goalie_stats,
df_team_info,
df_game_officials,
df_game_scratches, 
df_game_skater_stats]

def perc_null(X):
    
    total = X.isnull().sum().sort_values(ascending=False)
    data_types = X.dtypes
    percent = (X.isnull().sum()/X.isnull().count()).sort_values(ascending=False)

    missing_data = pd.concat([total, data_types, percent], axis=1, keys=['Total','Type' ,'Percent'])
    return missing_data

#for X in data_frames:
#    print(perc_null(X)['Total'].sum())

##goalie stats, skater stats, team_stats all have NaN ... 
## I think missing vals are in df_mp ... deal later
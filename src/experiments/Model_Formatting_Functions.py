###  model version 1. home and away with +1/-1

##we assume imput is df with labels as in our main df; in general one could ask for vars with names of key vars
def make_HA_data(X, list_vars = ['Date', 'season',
 'game_id',
 'mp_date',
 'nhl_name',
 'team_id',
 'HoA',
 'won',
 'settled_in',
 'goalsFor',
 'goalsAgainst'] ): #,  playoffs = False, list_seasons =[20162017] ):
    pass
##assumptions 

#sorted(list(X.columns))

#X_2016.loc[~(X_2016.sort_values(by = ['game_id'])['game_id'].values == X_2016.sort_values(by = ['mp_date', 'game_id'])['game_id'].values), :]


##these two functions 
# assign game_id to df_betting ... using two different look up tables, df_game and df_mp_teams
##note the following error codes are assigned if a game is not found or found more than once 
# if a home game is empty: 80    #8 is for h
# if a home game has >= 2 entries: 82
# if an away game is empty: 10   #1 is for a
# if an away game has >= 12 entries: 82

def mp_to_bet_add_game_id(df_mp_teams, mp_date, nhl_name, VH):##put VH in there! duh
    if VH == 'H':
        h = df_mp_teams.loc[(df_mp_teams['mp_date'] == mp_date)&(df_mp_teams['nhl_name'] == nhl_name)&(df_mp_teams['home_or_away'] == 'HOME'),  :]['game_id'].values
        if len(h) ==1:
            return h[0]
        elif len(h)==0 and mp_date < 2010000:
            return 80   
            print(mp_date)
        elif len(h) > 1:
            return 82
    if VH == 'V':
        a = df_mp_teams.loc[(df_mp_teams['mp_date'] == mp_date)&(df_mp_teams['nhl_name'] == nhl_name)&(df_mp_teams['home_or_away'] == 'AWAY'),  :]['game_id'].values
        if len(a) ==1:
            return a[0]
        elif len(a)==0:
            return 10   
        elif len(a) > 1:
            return 12

def game_to_bet_add_game_id(df_game, mp_date, nhl_name, VH):##put VH in there! duh
    if VH == 'H':
        ## this h and (also a) is an array of values ... it  may be empty; we expect exactly one element; might have >=2 or 0  if something is wrong
        h = df_game.loc[(df_game['mp_date'] == mp_date)&(df_game['nhl_name_home_team'] == nhl_name),  :]['game_id'].values
        if len(h) ==1:
            return h[0]
        elif len(h)==0:  #and mp_date < 2010000:
            return 80
            print(mp_date)
        elif len(h) > 1:
            return 82
    if VH == 'V':
        a = df_game.loc[(df_game['mp_date'] == mp_date)&(df_game['nhl_name_away_team'] == nhl_name),  :]['game_id'].values
        if len(a) ==1:
            return a[0]
        elif len(a)==0:
            return 220
        elif len(a) > 1:
            return 222


import tomli
import pathlib
import pandas as pd
import pickle

pkl_path = pathlib.Path('./test_sets.pkl')
with open(pkl_path, 'rb') as f:
    sets = pickle.load(f)
    print(f"sets: {sets}")


name_of_set = sets[0]['fullRoundText']
player_1 = sets[0]['slots'][0]['entrant']['name']
player_2 = sets[0]['slots'][1]['entrant']['name']
print(f"name of set : {name_of_set}")
print(f"name of player 1 : {player_1}")
print(f"name of player 2 : {player_2}")

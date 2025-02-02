from startggapi import StartGGAPI
# from startggapi._apis import TournamentApi
import tomli
import pathlib
import pandas as pd
import pickle


path_config = pathlib.Path('./config.toml')
print(path_config)
with open(path_config, "rb") as f:
    toml_dict = tomli.load(f)

startgg_token = toml_dict.get('TOKEN_STARTGG')['start_gg_token']
tournament_slug = toml_dict.get('STARTGG_TOURNAMENT_SLUG')['startgg_slug']

print(startgg_token)
api = StartGGAPI(startgg_token)
print(api)
toto = api.tournament.find_tournament_by_slug(tournament_slug)
id_ssbu = toto['events'][0]['id']
print(f"id tournoi ssbu :{id_ssbu}")

prout = api.entrant.find_all_by_event_id(id_ssbu)
print(toto)

sets = api.event.fetch_sets(id_ssbu)
print(sets)
name_of_set = sets[0]['fullRoundText']
player_1 = sets[0]['slots'][0]['entrant']['name']
player_2 = sets[0]['slots'][1]['entrant']['name']
print(f"name of set : {name_of_set}")
print(f"name of player 1 : {player_1}")
print(f"name of player 2 : {player_2}")

path_pkl = pathlib.Path("./test_sets.pkl")
with open(path_pkl, 'wb') as f:
    pickle.dump(sets, f)



# sets_df = pd.DataFrame(sets)
# csv_path = pathlib.Path('test_set.json')
# sets_df.to_json(csv_path, index=False)
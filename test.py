import pathlib
import time
import tomli
from startggapi.startggapi import *

if __name__ == "__main__":

    path_config = pathlib.Path('./config.toml')
    with open(path_config, "rb") as f:
        toml_dict = tomli.load(f)

    startgg_token = toml_dict.get('TOKEN_STARTGG')['start_gg_token']
    api = StartGGAPI(api_key=startgg_token)
    # res_heavy = api.tournament.find_events_by_tournament_slug_heavy(tourney_slug="let-s-play-iv-2")
    # res_heavy = api.tournament.find_events_by_tournament_slug_heavy(tourney_slug="genesis-x2")
    res_heavy = api.tournament.find_events_by_tournament_slug_heavy(tourney_slug="gamescom-lan-x-cgn-open")
    print(res_heavy)

    res_sets_phase = api.event.fetch_sets_in_phase(phase_id=2761375)
    tmp_list = []
    print(res_sets_phase)


    def dict_clean(_sets: list):
        """
        Some games are not ready to be played yet so the value of player['entrant'] is a None
        so we create its value that is a dict with a key 'name' and the value "undetermined"
        otherwise it crashes when you want to get it.
        We create a better dict of sets to fit our existing solution.
        :param _sets:
        :return: cleaned sets
        """
        fullTextRound = ""
        player1 = ""
        player2 = ""
        list_all_sets = []
        for _set in _sets:
            fullTextRound = _set["fullRoundText"]
            for player in _set['slots']:
                if player['entrant'] is None:
                    player['entrant'] = {"name": "__undetermined__"}
            player1 = _set['slots'][0]['entrant']['name']
            player2 = _set['slots'][1]['entrant']['name']

            list_all_sets.append({"Match": fullTextRound, "Player_1": player1, "Player_2": player2})
        return list_all_sets


    for i, phase in enumerate(res_heavy[2]['phases']):
        print(f"index of i in phases: {i}")
        for j, pool in enumerate(phase['phaseGroups']['nodes']):
            print(f"index of j in phaseGroups: {j}")
            res_sets_phase = api.event.fetch_sets_in_phase(phase_id=pool['id'])
            time.sleep(3)
            for k, match in enumerate(res_sets_phase):
                print(f"index of k in sets in a phase: {k}")
                print(match)
                for player in match['slots']:
                    if player['entrant'] is None:
                        player['entrant'] = {"name": "__undetermined__"}
                tmp_list.append({
                    "phase": phase['name'],
                    "pool": pool['displayIdentifier'],
                    "fullRoundText": match['fullRoundText'],
                    "player1": match['slots'][0]['entrant']['name'],
                    "player2": match['slots'][1]['entrant']['name'],
                    "totalGames": match['totalGames']
                })
    print(tmp_list)
    print(tmp_list)

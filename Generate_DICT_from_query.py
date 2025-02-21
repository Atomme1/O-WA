import time

from startggapi import StartGGAPI
# from startggapi._apis import TournamentApi
import tomli
import pathlib
import pickle


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


def get_event_id_by_tournament_slug(_api, _tournoi: dict, _startgg_event_name_slug: str) -> str:
    """
    Why do we have this shit ?
    Answer, people don't like to retrieve every information in a single query TO MAKE MY LIFE EASIER.
    So in order to get the sets of an event in a tournament, I need the ID of said event.
    Because the event slug is not in _tournoi, I need to get_event_details to get the slug and compare it to
    _startgg_event_name_slug
    But what for ? ==> getting the sets (matches) of an event
    :param _api:
    :param _tournoi:
    :param _startgg_event_name_slug:
    :return:
    """
    for event in _tournoi["events"]:
        event_info = _api.event.get_event_details(event["id"])
        event_slug = event_info["data"]["event"]["slug"]
        if _startgg_event_name_slug in event_slug:
            return event_info["data"]["event"]["id"]


def get_pkl_of_matches():
    """
    - Parses the config.toml
    - Get list of events in a tournament
    - Get ID of event desired
    - Get sets of ID event
    - Clean sets result
    - Returns a pickle of sets to be diplayed in table.html
    :return:
    """
    path_config = pathlib.Path('./config.toml')
    # print(path_config)
    with open(path_config, "rb") as f:
        toml_dict = tomli.load(f)

    startgg_token = toml_dict.get('TOKEN_STARTGG')['start_gg_token']
    startgg_link = toml_dict.get('STARTGG_TOURNAMENT_SLUG')['startgg_link']

    # Exemple of link ==> https://www.start.gg/tournament/genesis-x2/event/ultimate-singles
    startgg_link_slug_all = startgg_link.split("tournament/")[-1]
    startgg_tournament_slug = startgg_link_slug_all.split("/event/")[0]
    startgg_event_name_slug = startgg_link_slug_all.split("/event/")[-1]
    start_time = time.time()

    api = StartGGAPI(startgg_token)

    tournoi = api.tournament.find_tournament_by_slug(startgg_tournament_slug)
    print(f"tournoi['events'] = {tournoi['events']}")

    event_id = get_event_id_by_tournament_slug(_api=api,
                                               _tournoi=tournoi,
                                               _startgg_event_name_slug=startgg_event_name_slug)

    sets = api.event.fetch_sets(event_id)
    end_time = time.time()
    print(f"delta time IN QUERY = {end_time - start_time}")
    """    
    # name_of_set = sets[0]['fullRoundText']
    # player_1 = sets[0]['slots'][0]['entrant']['name']
    # player_2 = sets[0]['slots'][1]['entrant']['name']
    # print(f"name of set : {name_of_set}")
    # print(f"name of player 1 : {player_1}")
    # print(f"name of player 2 : {player_2}")
    """
    clean_sets = dict_clean(sets)

    path_pkl = pathlib.Path("./sets_of_tournament.pkl")
    with open(path_pkl, 'wb') as f:
        pickle.dump(clean_sets, f)


def get_top_8():
    return True


if __name__ == '__main__':
    get_pkl_of_matches()

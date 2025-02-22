import time

from startggapi.startggapi import *

if __name__ == "__main__":
    api = StartGGAPI(api_key="859b167984d46cef5f13c8511713d8f0")
    # res_heavy = api.tournament.find_events_by_tournament_slug_heavy(tourney_slug="let-s-play-iv-2")
    res_heavy = api.tournament.find_events_by_tournament_slug_heavy(tourney_slug="genesis-x2")
    print(res_heavy)
    # res_old = api.tournament.find_events_by_tournament_slug(tourney_slug="let-s-play-iv-2")
    # print(res_old)
    # res_fetch_old = api.event.fetch_sets(event_id=res_heavy[1]['id'])
    # for phase in res_heavy[3]['phases']:
    #     for pool in phase:
    #         res_sets_phase = api.event.fetch_sets_in_phase(phase_id=1780449)
    #         print(res_sets_phase)
    res_sets_phase = api.event.fetch_sets_in_phase(phase_id=2761375)
    tmp_list = []
    print(res_sets_phase)
    for i, phase in enumerate(res_heavy[3]['phases']):
        print(f"index of i in phases: {i}")
        for j, pool in enumerate(phase['phaseGroups']['nodes']):
            print(f"index of j in phaseGroups: {j}")
            res_sets_phase = api.event.fetch_sets_in_phase(phase_id=pool['id'])
            time.sleep(0.8)
            for k, match in enumerate(res_sets_phase):
                print(f"index of k in sets in a phase: {k}")
                print(match)
                tmp_list.append({
                    "phase": phase['name'],
                    "pool": pool['displayIdentifier'],
                    "fullRoundText": match['fullRoundText'],
                    "player1": match['slots'][0]['entrant']['name'],
                    "player2": match['slots'][1]['entrant']['name'],
                })
    print(tmp_list)
    print(tmp_list)

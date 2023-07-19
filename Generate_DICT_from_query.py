import pysmashgg
import pandas as pd
import pickle


# This code allows you to generate a CSV from pysmashgg functions query and use this CSV inside the ScoreBoard App,
# it will go through pages, more recent being 0 or 1 to n number of matchs)
# For example if your tournament has 64 players you will have 32 WinnerRound1 sets to played and the same number for
# LoserRound1.
# The variable "perPage" inside the function and the query made by pysmashgg allows to retrieve only 18 sets
# (if you want more like 37 as I did, go in the code and wiggle around the query and test the limit)
# Do quick a math of how many matches is there to be played and the number of pages you will input.
# 18*2 = 36 sets so you range must be 2 if you want all the matches from WinnerRound1

def print_hi(name):
    print(f'Hi, {name}')


def get_pkl_of_matches():
    with open('TOKEN_STARTGG.txt', 'r') as file:
        token = file.read().rstrip()
    smash = pysmashgg.SmashGG(token, True)

    fullSetsInTournamentEvent = []
    fullTextRound = []
    fullEntrant1Name = []
    fullEntrant2Name = []

    for i in range(0, 5):
        sets = smash.tournament_show_sets("let-s-play-v", "1v1-smash-ultimate", i)

        for set in sets:
            # print(set['fullRoundText'] + "  player 1: " + set['entrant1Name'] + "  player 2: " + set['entrant2Name'])
            fullSetsInTournamentEvent.append(set)
            fullTextRound.append(set['fullRoundText'])
            fullEntrant1Name.append(set['entrant1Name'])
            fullEntrant2Name.append(set['entrant2Name'])
            #print(set)
    print(len(fullSetsInTournamentEvent))

    data_lp = {"Match": fullTextRound, "Player_1": fullEntrant1Name, "Player_2": fullEntrant2Name}
    df_data_lp = pd.DataFrame(data_lp)
    # df_data_lp.to_csv("data_lp.csv", sep=';', encoding='utf-8', index=False)
    matchs = df_data_lp.to_dict(orient='records')
    print(df_data_lp)
    with open('data_lp_3.pkl', 'wb') as f:
        pickle.dump(matchs, f)


def get_top_8():
    return True


if __name__ == '__main__':
    get_pkl_of_matches()

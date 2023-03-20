import pysmashgg
import self as self
import json


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    with open('TOKEN_STARTGG.txt', 'r') as file:
        token = file.read().rstrip()
        print(token)
    smash = pysmashgg.SmashGG(token, True)
    # Shows a complete list of bracket ids given tournament and event names
    brackets = smash.tournament_show_event_brackets("let-s-play-ii", "1v1-smash-ultimate")
    print(brackets)
    print(brackets['bracketIds'][0])
    idBracket = brackets['bracketIds'][0]
    sets = smash.tournament_show_sets("let-s-play-ii", "1v1-smash-ultimate", 1)
    print(sets)
    for set in sets:
        print(set)

    print(len(sets))

    # parsed = json.loads(sets)
    # print(json.dumps(parsed, indent=4))

# {
#   "phaseId": 1308067,
#   "page": 1,
#   "perPage": 15,
#   "tournamentSlug": "let-s-play-ii",
#   "eventSlug": "1v1-smash-ultimate"
# }

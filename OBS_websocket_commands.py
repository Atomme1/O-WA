import time
import obswebsocket
from obswebsocket import obsws, requests  # noqa: E402
import json

with open('TOKEN_OBS_WEB-SOCKET.txt', 'r') as file:
    password = file.read().rstrip()

with open('IPV4.txt', 'r') as file:
    IPv4 = file.read().rstrip()

## VARIABLE
"""
You are forced to  e x p l i c i t l y  write down every source of OBS you will modify

To make things things easier for you, every functions in this project are not connected to each other
So
There is always a try catch with the obs part in case things go bad :eyes:
"""

_source1_name = "JOUEUR_GAUCHE"
_source2_name = "JOUEUR_DROITE"
_source3_name = "ROUND_TOURNOI"
_source4_name = "SCORE_GAUCHE"
_source5_name = "SCORE_DROITE"


# # Connect to the OBS Studio WebSocket server
# ws = obswebsocket.obsws(IPv4, 4444, password)
# ws.connect()

def swap_text_sources(ws, source1_name, source2_name):
    # Get the current text contents of the two sources
    source1_props = ws.call(obswebsocket.requests.GetTextGDIPlusProperties(source=source1_name))
    print(source1_props.datain['text'])
    source2_props = ws.call(obswebsocket.requests.GetTextGDIPlusProperties(source=source2_name))
    print(source2_props.datain['text'])

    source1_text = source1_props.datain['text']
    source2_text = source2_props.datain['text']
    print("nouveau text 1 " + source1_text)
    print("nouveau text 2 " + source2_text)
    # Set the text contents of the sources to each other's text
    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source=source1_name, text=source2_text))
    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source=source2_name, text=source1_text))


def rename_players(source1_name, source2_name, source1_text, source2_text):
    ws = obswebsocket.obsws(IPv4, 4444, password)
    ws.connect()

    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source=source1_name, text=source2_text))
    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source=source2_name, text=source1_text))
    ws.disconnect()


def rename_players_and_match(ws, source1_name, source2_name, source3_name, source1_text, source2_text, source3_text):
    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source=source1_name, text=source1_text))
    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source=source2_name, text=source2_text))
    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source=source3_name, text=source3_text))


def obs_do_swap_of_players():
    # Set the contents of a text file in OBS Studio
    ws = obswebsocket.obsws(IPv4, 4444, password)
    ws.connect()
    try:
        # scenes = ws.call(requests.GetSceneList())
        # print(scenes)

        swap_text_sources(ws, _source1_name, _source2_name)

        # ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source="textTestAPI", text="Hello, world!"))

    except KeyboardInterrupt:
        pass
    # Disconnect from the WebSocket server
    ws.disconnect()


def reset_scores(ws, _source4_name, _source5_name):
    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source=_source4_name, text="0"))
    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source=_source5_name, text="0"))
    return True


def obs_confirm_next_game(source1_text, source2_text, source3_text):
    ws = obswebsocket.obsws(IPv4, 4444, password)
    ws.connect()
    try:
        # scenes = ws.call(requests.GetSceneList())
        # print(scenes)

        rename_players_and_match(ws, _source1_name, _source2_name, _source3_name, source1_text, source2_text,
                                 source3_text)
        reset_scores(ws, _source4_name, _source5_name)
        # ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source="textTestAPI", text="Hello, world!"))

    except KeyboardInterrupt:
        pass
    # Disconnect from the WebSocket server
    ws.disconnect()


def add_1_player(ws, source_name: str, ):
    source_props = ws.call(obswebsocket.requests.GetTextGDIPlusProperties(source=source_name))
    source_text = str(int(source_props.datain['text']) + 1)  # changed str to int to str
    print("Plus 1" + source_text)
    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source=source_name, text=source_text))
    return True


def minus_1_player(ws, source_name):
    source_props = ws.call(obswebsocket.requests.GetTextGDIPlusProperties(source=source_name))
    source_text = str(int(source_props.datain['text']) - 1)
    print("Plus 1" + source_text)
    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source=source_name, text=source_text))
    return True


def obs_add_1_player_1():
    ws = obswebsocket.obsws(IPv4, 4444, password)
    ws.connect()
    try:
        # scenes = ws.call(requests.GetSceneList())
        # print(scenes)

        add_1_player(ws, _source4_name)

        # ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source="textTestAPI", text="Hello, world!"))

    except KeyboardInterrupt:
        pass
    # Disconnect from the WebSocket server
    ws.disconnect()


def obs_add_1_player_2():
    ws = obswebsocket.obsws(IPv4, 4444, password)
    ws.connect()
    try:
        # scenes = ws.call(requests.GetSceneList())
        # print(scenes)

        add_1_player(ws, _source5_name)

        # ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source="textTestAPI", text="Hello, world!"))

    except KeyboardInterrupt:
        pass
    # Disconnect from the WebSocket server
    ws.disconnect()


def obs_minus_1_player_1():
    ws = obswebsocket.obsws(IPv4, 4444, password)
    ws.connect()
    try:
        # scenes = ws.call(requests.GetSceneList())
        # print(scenes)

        minus_1_player(ws, _source4_name)

        # ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source="textTestAPI", text="Hello, world!"))

    except KeyboardInterrupt:
        pass
    # Disconnect from the WebSocket server
    ws.disconnect()


def obs_minus_1_player_2():
    ws = obswebsocket.obsws(IPv4, 4444, password)
    ws.connect()
    try:
        # scenes = ws.call(requests.GetSceneList())
        # print(scenes)

        minus_1_player(ws, _source5_name)

        # ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source="textTestAPI", text="Hello, world!"))

    except KeyboardInterrupt:
        pass
    # Disconnect from the WebSocket server
    ws.disconnect()

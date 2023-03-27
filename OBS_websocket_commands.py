import time
import obswebsocket
from obswebsocket import obsws, requests  # noqa: E402
import json

with open('TOKEN_OBS_WEB-SOCKET.txt', 'r') as file:
    password = file.read().rstrip()


with open('IPV4.txt', 'r') as file:
    IPv4 = file.read().rstrip()


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


# # Connect to the OBS Studio WebSocket server
# ws = obswebsocket.obsws(IPv4, 4444, password)
# ws.connect()

def rename_players(source1_name, source2_name, source1_text, source2_text):
    ws = obswebsocket.obsws(IPv4, 4444, password)
    ws.connect()

    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source=source1_name, text=source2_text))
    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source=source2_name, text=source1_text))
    ws.disconnect()

def do_swap_of_players():
    # Set the contents of a text file in OBS Studio
    ws = obswebsocket.obsws(IPv4, 4444, password)
    ws.connect()
    try:
        # scenes = ws.call(requests.GetSceneList())
        # print(scenes)
        source1_name = "textTestAPI"
        source2_name = "textTestAPI_2"
        swap_text_sources(ws, source1_name, source2_name)

        # ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source="textTestAPI", text="Hello, world!"))

    except KeyboardInterrupt:
        pass
    # Disconnect from the WebSocket server
    ws.disconnect()

# client.call(requests.SetSourceSettings(
#                     sourceName="source-name",
#                     sourceSettings={"file": file_name}
#                     ))

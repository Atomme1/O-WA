import time
import obswebsocket
from obswebsocket import obsws, requests  # noqa: E402


def swap_text_sources(ws, source1_name, source2_name):
    # Get the current text contents of the two sources
    source1_props = ws.call(obswebsocket.requests.GetTextGDIPlusProperties(source1_name)).getSources()[0]
    source2_props = ws.call(obswebsocket.requests.GetTextGDIPlusProperties(source2_name)).getSources()[0]
    source1_text = source1_props["text"]
    source2_text = source2_props["text"]

    # Set the text contents of the sources to each other's text
    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source1_name, {"text": source2_text}))
    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source2_name, {"text": source1_text}))


# Connect to the OBS Studio WebSocket server
ws = obswebsocket.obsws("192.168.1.28", 4455)
ws.connect()

# Set the contents of a text file in OBS Studio
try:
    #scenes = ws.call(requests.GetSceneList())
    #print(scenes)
    source1_name = "textTestAPI"
    source2_name = "textTestAPI2"
    #swap_text_sources(ws, source1_name, source2_name)

    ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source="textTestAPI", text={"text": "Hello, world!"}))

except KeyboardInterrupt:
    pass
# Disconnect from the WebSocket server
ws.disconnect()

# client.call(requests.SetSourceSettings(
#                     sourceName="source-name",
#                     sourceSettings={"file": file_name}
#                     ))


# What is O-WA ?
![Screenshot](image_for_readMe/O-WA_logo_alpha.png)

O-WA (OBS Web App) is an easy to use Scoreboard and Streamdeck web app for OBS that changes name of players, scores and scenes.
It does API calls to StartGG to get the matches yet to be played\
I developped it for my association USDEM 404.


## Introduction

Let's say you want to create an OBS plugin but you don't have
the time or the ressources to do so (like me).

With OBS Docks there is no need to !!\
Because you will access your application through an URL which can be host locally

Using <b>Python</b>, <b>Flask</b>, <b>PySmashGG</b>, <b>obswebsocket</b> and a little of <b>HTML / CSS / JS</b> you can have a local website 
making API calls to a python program that either does a websocket call to OBS to change names, scores and scenes or another API call (with PySmashGG) to 
StartGG that generate a DICT of the matches to be played.
#### Add the web app using the docks functionality of OBS
![Screenshot](image_for_readMe/overview1.png)
#### Open the docks in OBS
![Screenshot](image_for_readMe/overview2.png)
#### See the result
![Screenshot](image_for_readMe/overview3.png)

## How to setup

### Prerequisites
You need to have a Python 3.8+ (i did not test it for older version)\
Clone the repo using ```git clone https://github.com/Atomme1/O-WA.git``` \
Then use ```pip install -r requirements.txt``` to install the dependencies
- Flask
- PySmashGG
- obswebsocket
- Pickle (for dict)
- Pandas (for csv)


### Installing
Step-by-step instructions on how to install this project.
Watch the video below :)\
(coming soon)

## Useful links

The main librairy used is PySmashGG :https://pypi.org/project/pysmashgg/
OBS-Websocket documentation https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md
The external software I used for keeping up with the score of the players: 
https://obsproject.com/forum/resources/another-scoreboard-application.827/ \
This simple scoreboard application allows me to load a CSV of the matches to be played.

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

Using <b>Python</b>, <b>Flask</b>, <b>startggapi</b>, <b>obswebsocket</b> and a little of <b>HTML / CSS / JS</b> you can have a local website 
making API calls to a python program that either does a websocket call to OBS to change names, scores and scenes or another API call (with startggapi) to 
StartGG that generate a DICT of the matches to be played.
#### Add the web app using the docks functionality of OBS
![Screenshot](image_for_readMe/overview1.png)
#### Open the docks in OBS
![Screenshot](image_for_readMe/overview2.png)
#### See the result
![Screenshot](image_for_readMe/overview3.png)

## How to setup
### Prerequisites
You need to have a Python 3.13+ (i did not test it for older version)
- Clone the repo using ```git clone https://github.com/Atomme1/O-WA.git``` 
- Then use ```pip install -r requirements.txt``` to install the dependencies
- Create an account on startgg and create a private token for making API calls.
- Then you need to create a `config.toml` file containing the informations below
#### config.toml example
````toml
[TOKEN_STARTGG]
start_gg_token = "<YOUR_TOKEN_HERE>"

[OBS_WEBSOCKET]
pwd_obs = "<YOUR_PWD_HERE>"
ipv4_obs = "localhost"

[STARTGG_TOURNAMENT_SLUG]
startgg_slug = "<YOUR_TOURNAMENT-SLUG_HERE>"
startgg_videogame_displayName = "Ultimate"
#startgg_videogame_displayName = "Mario Kart 8 Deluxe"
````
- After that you can run the flask server
#### Run it like a pro
```
flask --app .\FLASK_APP_OBS_STARTGG.py run --host=0.0.0.0 
```


## Useful links

The main librairy used is startggapi : https://github.com/Caja-de-Dano/StartGG-API

OBS-Websocket documentation https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md

The external software I used for keeping up with the score of the players: 
https://obsproject.com/forum/resources/another-scoreboard-application.827/ \
This simple scoreboard application allows me to load a CSV of the matches to be played, but it was limited and could not
be implemented inside OBS.

## Known issues

First of all, this small project is not going have major updates since I don't use it at larger scale.

But i know it's flawed in some aspects like :

- ### I don't find the matches for the players of <name of game> in the generated list of matches

#### SOLUTION :  Change `startgg_link` in `config.toml`

import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, session
from OBS_websocket_commands_v2 import obs_do_swap_of_players, obs_confirm_next_game, obs_add_1_player_1, \
    obs_minus_1_player_1, obs_add_1_player_2, obs_minus_1_player_2, obs_switch2scene, obs_get_all_scenes, \
    obs_confirm_next_guest, obs_hide_unhide_item
import pickle
from Generate_DICT_from_query import *
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['TEMPLATES_AUTO_RELOAD'] = True


def load_data_from_PKL_2_DICT():
    with open('data_lp_3.pkl', 'rb') as f:
        matchs = pickle.load(f)
    return matchs


# I forgor that the format was a List of Dict (～￣▽￣)～
def load_data_from_xlsx_2_DICT() -> list:
    df_guest = pd.read_excel("data_guest.xlsx", index_col=False)
    print(df_guest)
    list_guest = []
    for index, row in df_guest.iterrows():
        print(row["Guest"])
        list_guest.append({"Guest": row["Guest"]})
    print(list_guest)
    return list_guest


@app.route('/', methods=['GET', 'POST'])
def show_table():
    matchs = load_data_from_PKL_2_DICT()
    print(matchs)
    if request.method == 'POST':
        # Get row from table in html
        selected_row = request.form['selected_row']
        # Split the selected row data into match, player1name and player2name
        Match, Selected_player_1, Selected_player_2 = selected_row.split(';;')
        # Store the match, player1name and player2name in the session
        session['selected_match'] = Match
        session['selected_player_1'] = Selected_player_1
        session['selected_player_2'] = Selected_player_2
        # return 'Selected row processed'
    # Retrieve the name of player and matches from the session
    _selected_match = session.get('selected_match', '')
    _selected_player_1 = session.get('selected_player_1', '')
    _selected_player_2 = session.get('selected_player_2', '')
    # rename_players("textTestAPI", "textTestAPI_2", _selected_player_1, _selected_player_2)
    print(type(_selected_match))
    return render_template('table.html', data=matchs, selected_match=_selected_match,
                           selected_player_1=_selected_player_1, selected_player_2=_selected_player_2)


@app.route('/table_ronde', methods=['GET', 'POST'])
def show_table_ronde():
    dict_guest = load_data_from_xlsx_2_DICT()
    print(dict_guest)
    if request.method == 'POST':
        # Get row from table in html
        selected_row = request.form['selected_row']
        session['selected_guest'] = selected_row
        # session['selected_guest'] = selected_row
        # return 'Selected row processed'
    # Retrieve the name of player and matches from the session
    _selected_guest = session.get('selected_guest', '')
    # rename_players("textTestAPI", "textTestAPI_2", _selected_player_1, _selected_player_2)
    print(type(_selected_guest))

    return render_template('Table_ronde.html', data=dict_guest, selected_guest=_selected_guest)


@app.route('/confirm_next_game', methods=['POST', 'GET'])
def confirm_next_game():
    obs_confirm_next_game(session['selected_player_1'], session['selected_player_2'], session['selected_match'])

    return redirect(url_for("show_table"))


@app.route('/confirm_next_guest', methods=['POST', 'GET'])
def confirm_next_guest():
    obs_confirm_next_guest(session['selected_guest'])

    return redirect(url_for("show_table_ronde"))


@app.route('/swap_name_OBS', methods=['POST', 'GET'])
def swap_name_OBS():
    obs_do_swap_of_players()
    return redirect(url_for("show_table"))


@app.route('/get_csv', methods=['POST', 'GET'])
def get_csv():
    get_pkl_of_matches()
    time.sleep(10)
    return redirect(url_for("show_table"))


@app.route('/add_1_player_1', methods=['POST', 'GET'])
def add_1_player_1():
    obs_add_1_player_1()
    return redirect(url_for("show_table"))


@app.route('/minus_1_player_1', methods=['POST', 'GET'])
def minus_1_player_1():
    obs_minus_1_player_1()
    return redirect(url_for("show_table"))


@app.route('/add_1_player_2', methods=['POST', 'GET'])
def add_1_player_2():
    obs_add_1_player_2()
    return redirect(url_for("show_table"))


@app.route('/minus_1_player_2', methods=['POST', 'GET'])
def minus_1_player_2():
    obs_minus_1_player_2()
    return redirect(url_for("show_table"))


# switching html pages
@app.route('/go2streamDeck', methods=['POST', 'GET'])
def go2streamDeck():
    list_scenes = obs_get_all_scenes()
    return render_template("streamDeck.html", button_names=list_scenes)


@app.route('/go2tableRonde', methods=['POST', 'GET'])
def go2tableRonde():
    return redirect(url_for("show_table_ronde"))


@app.route('/go2table', methods=['POST', 'GET'])
def go2table():
    return redirect(url_for("show_table"))


@app.route('/button/<value>')
def button_route(value):
    obs_switch2scene(value)
    return redirect(url_for("go2streamDeck"))


@app.route('/hide_unhide', methods=['POST', 'GET'])
def button_hide_unhide_item():
    obs_hide_unhide_item()
    return redirect(url_for("show_table_ronde"))


# Load Browser Favorite Icon
@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='static/O-WA logo.png')


if __name__ == "__main__":
    app.run(host="0.0.0.0")

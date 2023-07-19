from flask import Flask, render_template, request, redirect, url_for, session
from OBS_websocket_commands_v2 import obs_do_swap_of_players, rename_players, obs_confirm_next_game, obs_add_1_player_1, obs_minus_1_player_1, obs_add_1_player_2, obs_minus_1_player_2
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


@app.route('/', methods=['GET', 'POST'])
def show_table():
    matchs = load_data_from_PKL_2_DICT()
    if request.method == 'POST':
        # Get row from table in html
        selected_row = request.form['selected_row']
        # Split the selected row data into name and age
        Match, Selected_player_1, Selected_player_2 = selected_row.split(';;')
        # Store the match, player1name and player2name in the session
        session['selected_match'] = Match
        session['selected_player_1'] = Selected_player_1
        session['selected_player_2'] = Selected_player_2
        # return 'Selected row processed'
    # Retrieve the name and age from the session
    _selected_match = session.get('selected_match', '')
    _selected_player_1 = session.get('selected_player_1', '')
    _selected_player_2 = session.get('selected_player_2', '')
    # rename_players("textTestAPI", "textTestAPI_2", _selected_player_1, _selected_player_2)

    return render_template('table.html', data=matchs, selected_match=_selected_match,
                           selected_player_1=_selected_player_1, selected_player_2=_selected_player_2)


@app.route('/confirm_next_game', methods=['POST', 'GET'])
def confirm_next_game():
    obs_confirm_next_game(session['selected_player_1'], session['selected_player_2'], session['selected_match'])

    return redirect(url_for("show_table"))


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
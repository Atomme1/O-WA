from flask import Flask, render_template, request, redirect, url_for, session
from OBS_websocket_commands import obs_do_swap_of_players, rename_players, obs_confirm_next_game
import pandas as pd
import pickle

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['TEMPLATES_AUTO_RELOAD'] = True


def load_data_from_PKL_2_DICT():
    with open('data_lp.pkl', 'rb') as f:
        matchs = pickle.load(f)
    return matchs


matchs = load_data_from_PKL_2_DICT()


@app.route('/table', methods=['GET', 'POST'])
def show_table():
    if request.method == 'POST':
        # Get row from table in html
        selected_row = request.form['selected_row']
        # Split the selected row data into name and age
        Match, Selected_player_1, Selected_player_2 = selected_row.split(',')
        # Store the name and age in the session
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

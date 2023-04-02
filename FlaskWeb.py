from flask import Flask, render_template, jsonify, request, redirect, url_for
import test
from Generate_DICT_from_query import *
from OBS_websocket_commands import obs_do_swap_of_players
import pandas as pd
import time

app = Flask(__name__)



def load_data_from_CSV():
    df_data_lp = pd.read_csv("data_lp.csv")
    matchs = df_data_lp.values.tolist()
    return matchs


@app.route('/')
def home():
    matchs = load_data_from_CSV()
    return render_template('testDocks.html', your_list=matchs)
    # return render_template("testDocks.html")


@app.route('/get_csv', methods=['POST', 'GET'])
def get_csv():
    get_pkl_of_matches()
    time.sleep(10)
    return redirect(url_for("home"))


@app.route('/get_top_8', methods=['POST', 'GET'])
def get_top8():
    get_top_8()
    return redirect(url_for("home"))


@app.route('/swap_name_OBS', methods=['POST', 'GET'])
def swap_name_OBS():
    obs_do_swap_of_players()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

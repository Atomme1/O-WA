from flask import Flask, render_template, jsonify, request
import test
from Generate_CSV_from_query import *
from OBS_websocket_commands import do_swap_of_players

app = Flask(__name__)


def printYoupi():
    a = "printYoupi"


@app.route('/')
def home():
    return render_template("testDocks.html")


@app.route('/get_csv', methods=['POST', 'GET'])
def get_csv():
    get_csv_of_matches()
    return render_template("testDocks.html")


@app.route('/get_top_8', methods=['POST', 'GET'])
def get_top8():
    get_top_8()
    return render_template("testDocks.html")


@app.route('/swap_name_OBS', methods=['POST', 'GET'])
def swap_name_OBS():
    do_swap_of_players()
    return render_template("testDocks.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

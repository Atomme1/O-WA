from flask import Flask, render_template, jsonify, request
import test
from Generate_CSV_from_query import *
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


app.run(host="0.0.0.0", port=80, debug=True)



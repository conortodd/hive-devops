from flask import Flask, jsonify
import json
import requests
import datetime as dt
from printStatement import print_version
from tempApi import getAverageTemp

app = Flask(__name__)

@app.route("/version")
def version_endpoint():
    text={'version': print_version('src/version-label.txt')}
    return jsonify(text)

@app.route("/temperature")
def temp_endpoint():
    return jsonify(getAverageTemp())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
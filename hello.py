import requests
from flask import Flask, json, request
app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return json.jsonify(message='hello world')
    if request.method == 'POST':
        return json.jsonify(request.json)


@app.route('/forward')
def forward():
    response = requests.post('http://requestb.in/xp45khxp')
    return json.jsonify(message=response.text)

if __name__ == '__main__':
    app.debug = True
    app.run()

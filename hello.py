import requests
from bson.json_util import dumps
from flask import Flask, json, request
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'world'
mongoDB = PyMongo(app)


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

@app.route('/db',methods=['GET', 'POST'])
def db():
    if request.method == 'GET':
        return json.jsonify(dumps(mongoDB.db.fruits.find()))
    if request.method == 'POST':
        return 'todo'

if __name__ == '__main__':
    app.debug = True
    app.run()

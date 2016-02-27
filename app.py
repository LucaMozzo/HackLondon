import flask
from flask import Flask, send_from_directory
from pymongo import MongoClient

app = Flask(__name__)
app.debug = True
db = MongoClient("52.17.26.163")['test']

def strip_mongoid(document):
    document.pop("_id")
    return document

@app.route("/")
def hello():
    return send_from_directory("","index.html")

@app.route("/<filename>")
def serve_file(filename):
    return send_from_directory("", filename)

@app.route("/somethingForTest")
def test():
    return "Testing"

@app.route("/getAllUsers")
def getAllUsers():
    all = db['users'].find()
    all_list = [strip_mongoid(x) for x in all]
    return flask.jsonify(users=all_list)

if __name__ == "__main__":
    app.run()
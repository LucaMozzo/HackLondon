import flask
from flask import Flask, send_from_directory, request
from pymongo import MongoClient, ReturnDocument

app = Flask(__name__)
app.debug = True
db = MongoClient("52.17.26.163")['test']

def set_db(new_db):
    global db
    db = new_db

def strip_mongoid(document):
    document.pop("_id")
    return document

def create_new_id(id_name):
    counter_doc = db.counters.find_one_and_update({"id":id_name},
                                                  {"$inc":{"seq":1}},
                                                  return_document=ReturnDocument.AFTER,
                                                  upsert=True)
    return counter_doc['seq']

def create_new_task(task_name, date):
    name = task_name
    date = date
    id = create_new_id('taskId')
    return {"id": id, "name": name, "date": date}

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

@app.route("/addTask", methods = ['POST'])
def addTask():
    task = create_new_task(request.form['taskname'],
                           request.form['date'])
    db['tasks'].insert(task)
    return "Inserted "+str(task['id'])

@app.route("/adduser", methods = ['POST'])
def adduser():
    return str(request.form)

@app.route("/addTestTask", methods = ['GET'])
def addTestTask():
    task = create_new_task("testname", "testdate")
    db['tasks'].insert(task)
    return "Inserted "+str(task['id'])

if __name__ == "__main__":
    app.run()
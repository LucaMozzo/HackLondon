from flask import Flask, send_from_directory
app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return send_from_directory("","index.html")

if __name__ == "__main__":
    app.run()
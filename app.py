from flask import Flask, send_from_directory
app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return send_from_directory("","index.html")

@app.route("/<filename>")
def serve_file(filename):
    return send_from_directory("", filename)

@app.route("/somethingForTest")
def test():
    return "Testing"

if __name__ == "__main__":
    app.run()
import time
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def homepage():
    return "Hello"


@app.route("/about")
def about():
    time.sleep(0.01)
    return "About"


@app.route("/form", methods=["POST"])
def form():
    print(request.data)
    return "Thanks"


@app.route("/admin")
def admin():
    return "Forbidden", 403

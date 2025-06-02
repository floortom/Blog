import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

entries = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        reqCont = request.form.get("content")
        date = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((reqCont, date))

    entriesWithDate = [
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(entry[1], "%Y-%m-%d").strftime("%b %d")
        )
        for entry in entries
    ]

    return render_template("home.html", entries=entriesWithDate)

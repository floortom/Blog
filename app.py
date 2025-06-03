import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MONGODB_HOST = "localhost"
# MONGODB_PORT = 27017

client = MongoClient("mongodb://localhost:27017")
app.db = client["Ideas"]

@app.route("/", methods=["GET", "POST"])
def home():
    # print(client.list_database_names())
    if request.method == "POST":
        reqCont = request.form.get("content")
        date = datetime.datetime.today().strftime("%Y-%m-%d")
        app.db["Arbo"].insert_one({"content": reqCont,
                                   "date": date,
                                   })

    entriesWithDate = [
        (
            entry["content"],
            entry["date"],
            datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
        )
        for entry in app.db["Arbo"].entries.find({})
    ]

    return render_template("home.html", entries=entriesWithDate)

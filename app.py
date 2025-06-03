import datetime
import os
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    # MONGODB_HOST = "localhost"
    # MONGODB_PORT = 27017

    client = MongoClient(os.getenv("MONGODB_URI"))
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
            for entry in app.db["Arbo"].find({})
        ]
        # print(entriesWithDate)

        return render_template("home.html", entries=entriesWithDate)
    return app
from flask import Flask, render_template, request, redirect
from pony.orm import *

db = Database()
app = Flask(__name__)

class Pessoa(db.Entity):
    username = Required(str)
    email = Required(str)
    password = Required()

    def __str__(self):
        return {self.username}

@app.route("/")
def home():
    return render_template ("homepage.html")

@app.route("/aboutus")
def about():
    return render_template("about.html")

@app.route("/search")
def search():
    return render_template("search.html")
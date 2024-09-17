from flask import Flask, render_template, request, redirect
from pony.orm import *

db = Database()
app = Flask(__name__)

db.bind(provider='sqlite', filename='plantas.db', create_db=True)
db.generate_mapping(create_tables=True)

class Planta(db.Entity):
    nomedaplanta = Required(str)
    nomecientífico = Required(str)
    infonutri = Required(str)
    descricao = Required(str)
    receitas = Required(str)

@app.route("/")
def home():
    return render_template ("homepage.html")

@app.route("/aboutus")
def about():
    return render_template("about.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/form")
def form():
    return render_template("cadastro.html")

@app.route("/cadastrarplanta")
def cadastrar():
    nomeplanta=request.args.get("plantname")
    nomecientifico=request.args.get("cientifico")
    infonutri=request.args.get("infonutri")
    descricao=request.args.get("descricao")
    receitas=request.args.get("receitas")

    with db_session:
        p= Planta(nomeplanta=nomeplanta, nomecientifico=nomecientifico,infonutri=infonutri, descricao=descricao, receitas=receitas)
        commit()
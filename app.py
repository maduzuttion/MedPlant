#importar flask e pony
from flask import Flask, render_template, request, redirect
from pony.orm import *

#criação do banco de dados
db = Database()
app = Flask(__name__)

db.bind(provider='sqlite', filename='plantas.db', create_db=True)
db.generate_mapping(create_tables=True)

#criação da entidade "planta" do banco de dados
class Planta(db.Entity):
    nomedaplanta = Required(str)
    nomecientífico = Required(str)
    infonutri = Required(str)
    descricao = Required(str)
    indicacoes = Required(str)
    receitas = Required(str)

#rota principal
@app.route("/")
def home():
    return render_template ("homepage.html")

#rota sobre nós
@app.route("/aboutus")
def about():
    return render_template("about.html")

#rotas de pesquisa
@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/pesquisar")
def pesquisar():
    pesquisa=request.args.get("txtBusca")

#rotas de cadastro de nova planta
@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/cadastrarplanta")
def cadastrar():
    nomeplanta=request.args.get("plantname")
    nomecientifico=request.args.get("cientifico")
    infonutri=request.args.get("infonutri")
    descricao=request.args.get("descricao")
    indicacoes=request.args.get("indicacoes")
    receitas=request.args.get("receitas")

    with db_session:
        p=Planta(nomeplanta=nomeplanta, nomecientifico=nomecientifico,infonutri=infonutri, descricao=descricao, indicacoes=indicacoes, receitas=receitas)
        commit()
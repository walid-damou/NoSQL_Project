from flask import Flask , render_template
from pymongo import MongoClient

app = Flask(__name__)
#----------------------------Connexion avec MongoDB--------------------------------#
client = MongoClient()
client = MongoClient('localhost', 27017) #27017 port
db = client.gestionProduits #database gestionProduits 

produits = db.produits 
categorie = db.categorie 
utilisateurs = db.utilisateurs 

produits.find_one()
print(produits.find_one())
print("------------------Done-------------------")
#----------------------------/Connexion avec MongoDB--------------------------------#

#----------------------------Login--------------------------------#

@app.route("/")
def login():
    return render_template("login.html")

#----------------------------/Login--------------------------------#

#----------------------------HOME--------------------------------#

@app.route("/home")
def home():
    return render_template("index.html")

#----------------------------/HOME--------------------------------#

#----------------------------ADD Prod --------------------------------#

@app.route("/addProduit")
def AddProd():
    return render_template("addProduct.html")

#----------------------------/ADD Prod--------------------------------#

#----------------------------Update Prod--------------------------------#

@app.route("/addProduit")
def UpdateProd():
    return render_template("updateProduct.html")

#----------------------------/Update Prod--------------------------------#
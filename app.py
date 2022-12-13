from flask import Flask , render_template , request
from pymongo import MongoClient

app = Flask(__name__)
#----------------------------Connexion avec MongoDB--------------------------------#
client = MongoClient()
client = MongoClient('localhost', 27017) #27017 port
db = client.gestionProduits #database gestionProduits 

produits = db.produits 
categorie = db.categorie 
utilisateurs = db.utilisateurs 
print("------------------connected-------------------")
#----------------------------/Connexion avec MongoDB--------------------------------#

#----------------------------Login--------------------------------#

@app.route("/")
def Login():
    return render_template("login.html")

#----------------------------/Login--------------------------------#

#----------------------------HOME--------------------------------#

@app.route("/home")
def Home():
    return render_template("index.html",title="Acceuil")

#----------------------------/HOME--------------------------------#

#----------------------------ADD Prod --------------------------------#

@app.route("/addProduct" , methods=['POST'])
def AddProd():
    # if request.method=="POST":
    #     libelle = request.form.get("libelle")
    #     prix = request.form.get("prix")
    #     dateachat = request.form.get("dateachat")
    #     #get categorie id
    #     categorieName = request.form.get("categorie")
    #     print("--------")
    #     idCategorie = categorie.find_one({'denomination':categorieName})['idCategorie']

    #     # save picture
    #     img = request.files["img"]
    #     img_name = img.filename
    #     img.save('./static/images/'+img_name)

    #     newProd ={
    #                 "libelle": libelle,
    #                 "prixUnitaire": prix,
    #                 "dateAchat": dateachat,
    #                 "photoProduit": img_name,
    #                 "idCategorie": idCategorie
    #             }

    #     x = produits.insert_one(newProd)
        
    return render_template("addProduct.html",title="Ajouter produit")

#----------------------------/ADD Prod--------------------------------#

#----------------------------Update Prod--------------------------------#

@app.route("/updateProduct")
def UpdateProd():
    return render_template("updateProduct.html",title="Modifier produit")

#----------------------------/Update Prod--------------------------------#

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
# ----------------------------Connexion avec MongoDB--------------------------------#
client = MongoClient()
client = MongoClient('localhost', 27017)  # 27017 port
db = client.gestionProduits  # database gestionProduits

produits = db.produits
categorie = db.categorie
utilisateurs = db.utilisateurs

# produits.find_one()
# print(produits.find_one())
print(produits.aggregate([{'$lookup':{'from':'categorie','localField':'idCategorie','foreignField':'idCategorie','as':'Categorie'}}]))
print("------------------Done-------------------")
# ----------------------------/Connexion avec MongoDB--------------------------------#

# ----------------------------Login--------------------------------#


@app.route("/")
def Login():
    return render_template("login.html")

# ----------------------------/Login--------------------------------#

# ----------------------------HOME--------------------------------#

@app.route("/home")
def Home():
    all_produits=produits.aggregate([{'$lookup':{'from':'categorie','localField':'idCategorie','foreignField':'idCategorie','as':'Categorie'}}])
    return render_template("index.html", title="Acceuil", produits=all_produits)

# ----------------------------/HOME--------------------------------#

# ----------------------------ADD Prod --------------------------------#


@app.route("/addProduct")
def AddProd():
    return render_template("addProduct.html", title="Ajouter produit")

# ----------------------------/ADD Prod--------------------------------#

# ----------------------------Update Prod--------------------------------#
@app.route("/updateProduct/<ref>",methods=["POST","GET"])
def UpdateProd(ref):
    if request.method=="POST":
        libelle=request.form["libelle"]
        prix=request.form["prix"]
        date=request.form["dateachat"]
        categorie=int(request.form["categorie"])
        produits.update_one({'reference':int(ref)},{'$set':{'libelle':libelle,'prixUnitaire':prix,'dateAchat':date,'idCategorie':categorie}})
        return Home()
    else:
        # prd = produits.find_one({'reference':int(ref)})
        prd=produits.aggregate([{'$match':{'reference':int(ref)}},{'$lookup':{'from':'categorie','localField':'idCategorie','foreignField':'idCategorie','as':'Categorie'}}])
        categories_list=db.categorie.find({'idCategorie':{'$ne':int(ref)}})
        for i in prd:
            theProduct=i
        return render_template("updateProduct.html", title="Modifier produit",produit=theProduct,categorieslist=categories_list)

# ----------------------------/Update Prod--------------------------------#

# ----------------------------/Delete Prod--------------------------------#

@app.route('/deleteProduct/<ref>')
def DeleteProd(ref):
    produits.delete_one({'reference':int(ref)})
    return Home()

# ----------------------------/Delete Prod--------------------------------#

if __name__ == "__main__":
    app.run(debug=True)

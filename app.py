from flask import Flask, render_template, request, request, session, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)
# ----------------------------Connexion avec MongoDB--------------------------------#
client = MongoClient()
client = MongoClient('localhost', 27017)  # 27017 port
db = client.get_database('gestionProduits')  # database gestionProduits
SESSION_TYPE = "redis"
PERMANENT_SESSION_LIFETIME = 1800

app.config.update(SECRET_KEY=os.urandom(24))

app.config.from_object(__name__)


produits = db.produits
categorie = db.categorie
utilisateurs = db.utilisateurs

# produits.find_one()
# print(categories.find_one({'idCategorie':1}))
# print("------------------Done-------------------")
# ----------------------------/Connexion avec MongoDB--------------------------------#

# ----------------------------Login--------------------------------#


@app.route("/", methods=['POST', 'GET'])
def Login():
    if "username" in session:
        return redirect(url_for("Home"))
    if request.method == "POST":
        user=request.form.get("username")
        password=request.form.get("password")
        user_found=utilisateurs.find_one({"username":user})
        if user_found:
            user_val=user_found["username"]
            password_check=user_found["password"]
            if password==password_check:
                session["username"]=user_val
                return redirect(url_for("Home"))
    return render_template('login.html')
    


# ----------------------------/Logout--------------------------------#

@app.route("/logout")
def Logout():
    session.pop('username', None)
    return redirect(url_for('Home'))


# ----------------------------HOME--------------------------------#

@app.route("/home")
def Home():

    if 'username' in session:
        username = session['username']
        all_produits=produits.aggregate([{'$lookup':{'from':'categorie','localField':'idCategorie','foreignField':'idCategorie','as':'Categorie'}},{'$addFields':{'Categorie':{'$arrayElemAt':["$Categorie",0]}}}])
        return render_template("index.html", title="Acceuil", produits=all_produits)
    else:
        return redirect(url_for('Login'))

    

# ----------------------------/HOME--------------------------------#

# ----------------------------ADD Prod --------------------------------#


@app.route("/addProduct" , methods=['POST',"GET"])
def AddProd():
    categories_list=db.categorie.find()
    if request.method=="POST":
        reference = produits.count_documents({})+1
        libelle = request.form.get("libelle")
        prix = request.form.get("prix")
        dateachat = request.form.get("dateachat")
        idCategorie = request.form.get("categorie")

        # save picture
        img = request.files["img"]
        img_name = img.filename
        img.save('./static/images/'+img_name)

        newProd ={
                    "reference" : reference,
                    "libelle": libelle,
                    "prixUnitaire": prix,
                    "dateAchat": dateachat,
                    "photoProduit": img_name,
                    "idCategorie": int(idCategorie)
                }

        x = produits.insert_one(newProd)
        
    return render_template("addProduct.html",title="Ajouter produit" , categoriesList=categories_list)

# ----------------------------/Update Prod--------------------------------#
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
# ----------------------------/Delete Prod--------------------------------#

@app.route('/deleteProduct/<ref>')
def DeleteProd(ref):
    produits.delete_one({'reference':int(ref)})
    return Home()

# ----------------------------/Delete Prod--------------------------------#

if __name__ == "__main__":
    app.run(debug=True)

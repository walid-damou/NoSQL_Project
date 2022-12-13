from flask import Flask , render_template

app = Flask(__name__)

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

#----------------------------ADD Prod--------------------------------#

@app.route("/addProduct")
def AddProd():
    return render_template("addProduct.html",title="Ajouter produit")

#----------------------------/ADD Prod--------------------------------#

#----------------------------Update Prod--------------------------------#

@app.route("/updateProduct")
def UpdateProd():
    return render_template("updateProduct.html",title="Modifier produit")

#----------------------------/Update Prod--------------------------------#

if __name__ == "__main__":
    app.run(debug=True)

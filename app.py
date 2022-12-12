from flask import Flask , render_template

app = Flask(__name__)

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

#----------------------------ADD Prod--------------------------------#

@app.route("/addProduit")
def AddProd():
    return render_template("addProduct.html")

#----------------------------/ADD Prod--------------------------------#

#----------------------------Update Prod--------------------------------#

@app.route("/addProduit")
def UpdateProd():
    return render_template("updateProduct.html")

#----------------------------/Update Prod--------------------------------#
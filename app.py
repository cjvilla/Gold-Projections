import os
import csv
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


################################################
# Create home page
#################################################
@app.route("/")
def home():
    return render_template("home.html")


################################################
# Create home page
#################################################
@app.route("/price")
def price():
    return render_template("goldprice.html")

################################################
# Create home page
#################################################
@app.route("/page2")
def page2():
    return render_template("page2.html")





##############################################
# Run App
##############################################

if __name__ == "__main__":
    app.run(debug=True)

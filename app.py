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







##############################################
# Run App
##############################################

if __name__ == "__main__":
    app.run(debug=True)

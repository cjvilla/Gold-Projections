import os
import csv
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Database setup
#################################################
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'postgresql+psycopg2://{os.getenv("gold")}:' +
    f'{os.getenv("b00tcamp1!")}@{os.getenv("gold-project.c58dxtfoq0r7.us-east-2.rds.amazonaws.com")}/{os.getenv("gold-project")}'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

################################################
# Create class to get Data
################################################
class Data(db.Model):
    __tablename__ = 'flask_data'

    Year = db.Column(db.String(4), primary_key=True)
    Month = db.Column(db.String(10), primary_key = True)
    Inflation_Value = db.Column(db.Numeric(2,2))
    dollar_index = db.Column(db.Numeric(3,5))
    us_dollar = db.Column(db.Numeric(3,5))
    pound = db.Column(db.Numeric(3,5)) 
    indian_rupee = db.Column(db.Numeric(5,5))
    south_african_rand = db.Column(db.Numeric(4,5)) 
    australian_dollar =  db.Column(db.Numeric(3,5)) 

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
@app.route("/graphs")
def pgraphs():
    return render_template("graphs.html")

################################################
# Create home page
#################################################
@app.route("/page2")
def page2():
    
    results = db.session.query(Data.Year, Data.Month, Data.Inflation_Value, Data.dollar_index, Data.us_dollar, Data.pound,
    Data.indian_rupee, Data.south_african_rand, Data.australian_dollar).all()

    print(results[0])

    return render_template('page2.html', data = results)


##############################################
# Run App
##############################################

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, render_template, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
from model import connect_to_db, db, Product

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""

    return render_template("index.html")


@app.route("/searchClothing")
def search_clothing():
    """Add a student."""
    
    search_item = request.args.get('myInput')
   
    # need to query database



    #payload = {'fts': description}

    #r = requests.get(url, params = payload)



    #return render_template("databaseResult.html",
                           #description=description, size=size, price=price)

@app.route("/searchData")
def search_data():
    """Add a student."""
    

    search_term = request.args.get('the-basics')
    results = Product.query.filter(Product.name.like('%' + search_term + '%')).all()
    #results = Product.query.filter(Product.name.op('~')('\Y' + search_term + '\y')).all()

    new_results = []
    for result in results[:10]:
        new_results.append(result.name) 
    #result = Product.query.filter(Product.name.contains(search_term)).first()
    return jsonify(new_results)






if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')

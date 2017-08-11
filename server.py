from flask import Flask, request, render_template
import requests
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

url = "http://api.shopstyle.com/api/v2/products?pid=uid6369-39701287-7"

@app.route('/')
def index():
    """Return homepage."""

    return render_template("index.html")



@app.route("/searchClothing")
def search_clothing():
    """Add a student."""
    
    description = request.args.get('description')
    size = request.args.get('size')
    price = request.args.get('price')
    payload ={'fts': description}
    r = requests.get(url, params = payload)



    return render_template("databaseResult.html",
                           description=description, size=size, price=price)




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

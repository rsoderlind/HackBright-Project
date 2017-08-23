from flask import Flask, request, render_template, jsonify, flash, redirect, session
import requests, os
from flask_sqlalchemy import SQLAlchemy
from model import connect_to_db, db, Product, User, User_Product

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""

    return render_template("index.html")


@app.route("/searchClothing")
def search_clothing():
    """Add a student."""
    
    search_item = request.args.get('myInput')

@app.route("/searchData")
def search_data():
    """Search Database"""
    

    search_term = request.args.get('the-basics')
    results = Product.query.filter(Product.name.like('%' + search_term + '%')).all()
    #results = Product.query.filter(Product.name.op('~')('\Y' + search_term + '\y')).all()

    new_results = []
    for result in results[:20]:
        new_results.append({"id": result.product_id, "name": result.name}) 
    #result = Product.query.filter(Product.name.contains(search_term)).first()
    print new_results
    return jsonify(new_results)


@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup."""

    return render_template("register_form.html")

@app.route('/display')
def display_products():
    """Display Products Searched For in Database."""

    user_id = session['user_id']
    
    #suggestions = User_Product.query.filter(User_Product.product_id==Product.product_id)

    saved_searches = User_Product.query.filter_by(user_id=user_id).all()

    name = db.session.query(User.name).filter(User.customer_id==user_id).first()[0]

    return render_template("display.html", saved_searches=saved_searches, name=name, suggestions=suggestions)

    


@app.route('/register', methods=['POST'])
def register_process():
    """Process registration."""

    # Get form variables
    email = request.form["email"]
    password = request.form["password"]
    name = request.form['name']
    new_user = User(email=email, password=password, name=name)

    db.session.add(new_user)
    db.session.commit()

    flash("User %s added." % email)
    return redirect("/login")


@app.route('/save', methods=['POST'])
def save_product():
    """Process registration."""

    user_id = session.get('user_id')
    if not user_id:
        return redirect('/login')
    product_id = request.form.get('product_id')
    search_term = request.form.get('search_term')
    new_user_product = User_Product(user_id=user_id, product_id=product_id, search_term=search_term)
    db.session.add(new_user_product)
    db.session.commit()

    return redirect(request.referrer)


@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login_form.html")


@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("No such user")
        return redirect("/register")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")

    session["user_id"] = user.customer_id

    flash("Logged in")
    return redirect("/")


@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")



if __name__ == "__main__":
    connect_to_db(app)
    app.config['SECRET_KEY'] = os.environ.get('APP_SECRETKEY')
    app.run(debug=True, host='0.0.0.0')

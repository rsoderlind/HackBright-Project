from flask import Flask, request, render_template, jsonify, flash, redirect, session
import requests, os
from flask_sqlalchemy import SQLAlchemy
from model import connect_to_db, db, Product, User, User_Product

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""

    image_results = db.session.query(Product).filter(Product.image != "").limit(10).all()
    id_results =   db.session.query(Product).filter(Product.product_id != 0).limit(10).all()  
    #new_image_results = []

    #for image in image_results[:10]:
     #   new_image_results.append({'image': image.image})
    
    return render_template("index.html", image_results=image_results, id_results=id_results)


@app.route('/seeNextTen')
def see_next_ten():
    """See Next Ten image items."""

    if 'button_click' in session:
        next_ten = session['button_click'] * 6
    else:
        next_ten = 0

    if 'button_click' not in session:
        session['button_click'] = 1
    else:
        session['button_click'] += 1


    image_results = db.session.query(Product).filter(Product.image != "").limit(6).offset(next_ten).all()
      
    new_image_results = []

    for image in image_results[:7]:
        new_image_results.append({'image': image.image})
    
    final_results = {'new_image_results': new_image_results}

    return jsonify(final_results)


@app.route("/searchClothing")
def search_clothing():
    """Add a student."""
    
    search_item = request.args.get('myInput')


@app.route("/getBestItems")
def get_best_items():    

    search_list = ["top", "skirt", "shoes", "pants", "blouse", "sneaker", "earrings", "jeans", "blazer", "jacket"]
    new_results = []

    for search_list_item in search_list:
        results = Product.query.filter(Product.name.like('%' + search_list_item + '%')).all()

        for result in results[:100]:
            new_results.append({"id": result.product_id, "name": result.name, "image": result.image})

    final_results = {'new_results': new_results}

    return jsonify(final_results)


@app.route("/searchData")
def search_data():
    """Search Database"""
    search_term = request.args.get('searchClothing')

    results = Product.query.filter(Product.name.like('%' + search_term + '%')).all()
    #results = Product.query.filter(Product.name.op('~')('\Y' + search_term + '\y')).all()

    #image_results = db.session.query(Product).filter(Product.image != "").all()    
    #new_image_results = []

    #for image in image_results[:10]:
     #   new_image_results.append({'image': image.image})

    new_results = []
    for result in results[:20]:
        new_results.append({"id": result.product_id, "name": result.name, "image": result.image}) 
    #result = Product.query.filter(Product.name.contains(search_term)).first()
    #print new_results

    prev_liked = db.session.query(Product).join(User_Product).filter(User_Product.search_term==search_term).all()

    prev_liked_ids = [product.product_id for product in prev_liked]

    other_products = db.session.query(Product).filter(Product.name.like('%' + search_term + '%'), 
                    ~ Product.product_id.in_(prev_liked_ids)).all()

    other_results = []
    for product in other_products[:10]:
        other_results.append({"id": product.product_id, "name": product.name})
    
    #final_results = {'other_results': other_results, 'new_results': new_results, 'new_image_results': new_image_results}
    final_results = {'other_results': other_results, 'new_results': new_results}

    return jsonify(final_results)


@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup."""

    return render_template("register_form.html")

@app.route('/display')
def display_products():
    """Display Products Searched For in Database."""

    user_id = session['user_id']
    
    saved_searches = User_Product.query.filter_by(user_id=user_id).all()

    name = db.session.query(User.name).filter(User.customer_id==user_id).first()[0]

    return render_template("display.html", saved_searches=saved_searches, name=name)

    


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
    product_id = request.form.get('result_id')
    search_term = request.form.get('search_term')
    new_user_product = User_Product(user_id=user_id, product_id=product_id, search_term=search_term)
    db.session.add(new_user_product)
    db.session.commit()

    return redirect(request.referrer)


@app.route('/displayModal', methods=['POST'])
def display_modal():
    """Process registration."""

    product_description = request.form.get('product_description')
    product_name = request.form.get('product_name')
    product_clickurl = request.form.get('product_clickurl')

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

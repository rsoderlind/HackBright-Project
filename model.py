from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# WRITE CLASSES HERE

class User(db.Model):
    """Users class."""

    __tablename__ = 'users'

    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    


class Product(db.Model):
    """Products class."""

    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500), nullable=False)
    currency = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    retailer = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    click_url = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(500), nullable=False)

class User_Product(db.Model):
    """User_Product class."""

    __tablename__ = 'users_products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.customer_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)

    # Define relationship to Product
    product = db.relationship("Product",
                           backref=db.backref("users_products", order_by=id))

    
        

# HELPERS
def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///products'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    db.create_all()
    print "Connected to DB."

"""Utility file to seed product database from ShopStyle Collective JSON data in seed_data/"""

from sqlalchemy import func
import requests, os
from model import User, Product, connect_to_db, db
from server import app


def load_products():
    api_key = os.environ.get('API_KEY')
    #url = "http://api.shopstyle.com/api/v2/products?pid=uid6369-39701287-7&limit=50&cat=athletic-pants"
    total_products = []
    limit = 50
    offset = 0
    while True:
        url ="http://api.shopstyle.com/api/v2/products?pid=" + api_key + "&limit=" + str(limit) + "&offset=" + str(offset)
        resp = requests.get(url)
        result = resp.json()
    
        products = result['products']
        
        total_products.extend(products)

        for product in total_products:
            product_id = product['id']
            product_name = product['name']
            product_currency = product['currency']
            product_price = product['price']
            product_retailer = product['retailer']['name']
            product_description = product['description']
            product_clickurl = product['clickUrl']
            product_image = product['image']['sizes']['Large']['url']

            new_product = Product(name = product_name, currency = product_currency, 
                              price = product_price, retailer = product_retailer, click_url = product_clickurl, image = product_image, description = product_description)

            db.session.add(new_product)
        db.session.commit()

        if len(products) < limit:
            break
        offset += limit
        total_products=[]


    #print type(products)
#products = load_products()


#first_product_dict = products[1]

#print first_product_dict['id']
#print first_product_dict['name']
#print first_product_dict['currency']
#print first_product_dict['price']
#print first_product_dict['retailer']
#print first_product_dict['description']
#print first_product_dict['clickUrl']
#print first_product_dict['image']['sizes']['Large']



if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()
    load_products()


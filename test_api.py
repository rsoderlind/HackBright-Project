import requests

def get_products():
    #url = "http://api.shopstyle.com/api/v2/products?pid=uid6369-39701287-7"
    #url = "http://api.shopstyle.com/api/v2/products?pid=uid6369-39701287-7&limit=50&cat=athletic-pants"
    url ="http://api.shopstyle.com/api/v2/products?pid=uid6369-39701287-7"
    resp = requests.get(url)
    result = resp.json()
    
    products = result['products']
    
    print type(products)
    return products


products = get_products()
#need to loop through all products

first_product_dict = products[1]
print first_product_dict['id']
print first_product_dict['name']
print first_product_dict['currency']
print first_product_dict['price']
print first_product_dict['retailer']
print first_product_dict['description']
print first_product_dict['clickUrl']
print first_product_dict['image']['sizes']['Large']

#first_size_dict =    first_product_dict['stock'][0]
#print first_product_dict['description'][0]
#print first_size_dict['size'][0]

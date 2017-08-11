import requests

def get_products():
    url = "http://api.shopstyle.com/api/v2/products?pid=uid6369-39701287-7"
    resp = requests.get(url)
    result = resp.json()
    
    products = result['products']
    
    print type(products)

    for item in products:
        print item, "\n\n\n\n\n\n"

    return products


products = get_products()
first_product_dict = products[0]
print first_product_dict['sizes']

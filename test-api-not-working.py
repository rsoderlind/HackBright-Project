import requests
from requests.auth import HTTPBasicAuth
import base64

def get_products():
    secret = '3Iu9+I7rwqtsvKxLuYnwmQ==:ba7bd3c6aa85b636eeecf7d3d0b675569def76e862777ea0ba799138cfacee83'
    access_key = 'AK8617ecb3d43eca1b46dc4a63de0712d7'
    usrPass = access_key + ":" + secret
    b64Val = base64.b64encode(usrPass) 
    url = "https://blue-api.bodylabs.com/measurements/partial"
    payload = {
                'gender': 'female', 
                'measurements': {
                    'unitedStates':{
                        'height':60,
                        'weight':120
                        }
                    }
                }



    headers = {

                # "Authorization": "Basic %s" % b64Val,
                'Content-Type': 'application/json',
                'X-Requested-API-Version': 'v2'
              }
    resp = requests.post(url, params=payload, auth=(access_key, secret), headers=headers)
    import pdb; pdb.set_trace()
    print resp
    print resp.reason
    result = resp.json()
    products = result['data']
    print products

get_products()






#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
import sys
import cgi
from time import time_ns
from random import randint
import os

# takes the input and puts it into the DATA variable
data = cgi.FieldStorage() # {id: }

cookie_data = os.environ.get('HTTP_COOKIE')

sys.path.append("/Users/adrian/Desktop/PY-PROJECTS/Level 2/Data Base (DB)/e-shop")

cookie_data = os.environ.get('HTTP_COOKIE')

from orm.CartManager import CartManager
from orm.Client import Client
from orm.BagItem import *
product_id = data.getvalue('id')

CartManager.addItem(product_id)

# FORCE USER REDIRECT TO SIGN UP

print("Content-type: text/html;charset=UTF-8") # -> HTTP Heder (encoding for PY to HTML) 

if cookie_data !='':
    cookie_key, cookie_value = cookie_data.split('=')


    if cookie_key == 'client_id':
        print(f"Refresh: 0; URL=/web/catalog.py")
        client = Client.get(int(cookie_value))
        
        if client != None:
            #  BagItem(f"  {product_id},      10")
            #  CartManager.addItem()
             pass
            
else:
    # redirect to sign up
    print(f"Refresh: 0; URL=/web/sign-up.py?id={product_id}") # redirecting to details URL

    
print() # \n -> Marks HTTP header end



print(cookie_data)

print("ADD TO CART")
  
#print(cookie_key, cookie_value)
#print(f"Product {product_id}  HAS BEEN ADDED TO THE CART")
# print(f"You will be redirected to the product page in 3 secounds")
   



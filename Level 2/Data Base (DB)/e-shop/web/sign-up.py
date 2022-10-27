#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
import sys
import cgi
from time import time_ns
from random import randint


# takes the input and puts it into the DATA variable
data = cgi.FieldStorage() # {id: }

sys.path.append("/Users/adrian/Desktop/PY-PROJECTS/Level 2/Data Base (DB)/e-shop")

from orm.CartManager import CartManager
from orm.Client import Client

product_id = data.getvalue('id')
CartManager.addItem(product_id)
# HW1: finish the addItem() method

# print(f"Refresh: 3; URL=/web/details.py?id={product_id}") # redirecting to details URL
print("Content-type: text/html;charset=UTF-8") # -> HTTP Heder (encoding for PY to HTML) 

print() # \n -> Marks HTTP header end

#print(f"Product {product_id}  HAS BEEN ADDED TO THE CART")
# print(f"You will be redirected to the product page in 3 secounds")
print(
    f"""
    <h1> You must sign up to continue</h1>
    <form action= '/web/create-user.py'>
            <input name='name' type='text'placeholder= 'enter your name...'/><br>
            <input name='email' type='text'placeholder= 'enter your email...'/><br>
            <input name='phone' type='text'placeholder= 'enter your phone...'/><br>
            <input name='password' type='password'placeholder= 'enter your password...'/><br>
            <input name='id' type='hidden' value='{product_id}'><br>
            <button> SIGN UP </button>
    </form> 
    """
)
print(f"<a href='/web/catalog.py'>GO TO CATALOG</a><br>")




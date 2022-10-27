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

name = data.getvalue('name')
email = data.getvalue('email')
phone = data.getvalue('phone')
password = data.getvalue('password')
product_id =data.getvalue('id')


# 1. create an new client object + id
id = time_ns() * 10 + randint(0,9)
client = Client(
            id,
            name,
            email,
            phone,
            False,
            password # add hashing
)
client.create()
# 2. store in the datebase
# 3. send client in to the browser


print(f"Set-cookie: client_id={id};")
print(f"Refresh:1; URL=/web/add-to-cart.py?{product_id}") # redirecting to details URL
print("Content-type: text/html;charset=UTF-8") # -> HTTP Heder (encoding for PY to HTML) 

print() # \n -> Marks HTTP header end














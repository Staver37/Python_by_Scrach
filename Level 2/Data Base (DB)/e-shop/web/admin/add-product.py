#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
import sys
import cgi
from time import time_ns
from random import randint
import os

sys.path.append("/Users/adrian/Desktop/PY-PROJECTS/Level 2/Data Base (DB)/e-shop")
from orm.Product import *
from orm.ProductStock import *
data = cgi.FieldStorage() # {id: }


# takes the input and puts it into the DATA variable


cookie_data = os.environ.get('HTTP_COOKIE')

# HW: these verification should be on ALL admin pages
# if admin_id is in the cookies

# if cookie_data !='':
#     cookie_key, cookie_value = cookie_data.split('=')


#     if cookie_key == 'admin_id':
#         print(f"Refresh: 0; URL=/web/admin/sign-in.py")

print("Content-type: text/html;charset=UTF-8") # -> HTTP Heder (encoding for PY to HTML) 
       

id          = data.getvalue('id')
name        = data.getvalue('name')
price_value = data.getvalue('price_value')
price_unit  = data.getvalue('price_unit')
bar_code    = data.getvalue('bar_code')
quantity    = data.getvalue('quantity')


products = Product(
            id,
            name,
            price_value,
            price_unit,
            bar_code,
            quantity 
)
ProductStock.addProduct(products)


print(f"Refresh:0.1; URL=/web/admin/dashboard-prod.py")


print() # \n -> Marks HTTP header end

print(products)
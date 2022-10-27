#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3

########## MOVE dashboard.py IN ADMIN FOLDER  #############

import sys
import cgi
from time import time_ns
from random import randint
import os
sys.path.append("/Users/adrian/Desktop/PY-PROJECTS/Level 2/Data Base (DB)/e-shop")

from orm.ProductCatalog import ProductCatalog


data = cgi.FieldStorage() # {id: }


# takes the input and puts it into the DATA variable

price_sort = data.getvalue('price_sort')
products = ProductCatalog.index(price_sort if price_sort != None else "asc")

cookie_data = os.environ.get('HTTP_COOKIE')

# HW: these verification should be on ALL admin pages
# if admin_id is in the cookies

if cookie_data !='':
    cookie_key, cookie_value = cookie_data.split('=')


    if cookie_key == 'admin_id':
        print(f"Refresh: 0; URL=/web/admin/sign-in.py")



print("Content-type: text/html;charset=UTF-8") # -> HTTP Heder (encoding for PY to HTML) 
       

print() # \n -> Marks HTTP header end






print(f"<h1>🍗...ADMIN DASHBOARD FOR PRODUCTS...🍗</h1><br>")
print(f"<a href='/web/catalog.py'>GO TO CATALOG</a><br>")

print(f"<a href='/web/admin/sign-in.py'>GO TO SIGN_IN</a>")
# Stock Product  Table
print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <style>
        table, th, td , caption {
          border:1px solid black;
        }
        </style>
</head>
<body>
    <table>
        <tbody>
            <tr>
                <td>ID</td>
                <td>NAME</td>
                <td>PRICE_VALUE</td>
                <td>PRICE_UNIT</td>
                <td>BAR_CODE</td>
                <td>QUANTITY</td>
                <td>DELETE</td>
            </tr>   
''')           

for product in products:    
    print(f'''           
            <tr>
                    <td>{product.id} </td> 
                    <td>{product.name :30}</td>
                    <td>{product.price_value}</td>
                    <td>{product.price_unit}</td>
                    <td>{product.bar_code}</td>
                    <td>{product.quantity}</td> 
                    <td><a href='/web/admin/dellete-product.py?id={product.id}'a>delete</a></td>

            </tr>   
    ''')
print('''</tbody>       
           </tr>
        </table>
        </body>
        </html>
''')

print(
    f"""
    <h1> Add new produs in Stock</h1>
    
    <!-- Link to add-product-->
    
    <form action= '/web/admin/add-product.py'>                 
            <input name='id'          type='text'placeholder= 'Produce id...'/><br>
            <input name='name'        type='text'placeholder= 'Produce name...'/><br>
            <input name='price_value' type='text'placeholder= 'Price Value...'/><br>
            <input name='price_unit'  type='text'placeholder= 'Price Unit...'/><br>
            <input name='bar_code'    type='text'placeholder= 'Bar Code...'><br>
            <input name='quantity'    type='text'placeholder= 'Quantity...'><br> 
            <button> Add Produs </button>
    </form> 
    """
)


print(f"<a href='/web/admin/dashboard-client.py'>GO TO DASHBOARD CLIENT</a>")

# HW 
# - use the HTML table to show the product stock here 
# - name, q , operations

# - add a link to /web/add-product.py
# - make a from this page which will allow adding new products to stock

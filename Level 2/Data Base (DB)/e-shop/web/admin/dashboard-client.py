#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3

########## MOVE dashboard.py IN ADMIN FOLDER  #############

from http import client
import sys
import cgi
from time import time_ns
from random import randint
import os
sys.path.append("/Users/adrian/Desktop/PY-PROJECTS/Level 2/Data Base (DB)/e-shop")
from orm.Client import*
from orm.ProductCatalog import ProductCatalog


data = cgi.FieldStorage() # {id: }


# takes the input and puts it into the DATA variable

clients = Client.all()

cookie_data = os.environ.get('HTTP_COOKIE')

# HW: these verification should be on ALL admin pages
# if admin_id is in the cookies


# if cookie_data !='':
#     cookie_key, cookie_value = cookie_data.split('=')


#     if cookie_key == 'admin_id':
#         print(f"Refresh: 0; URL=/web/admin/sign-in.py")



print("Content-type: text/html;charset=UTF-8") # -> HTTP Heder (encoding for PY to HTML) 
       

print() # \n -> Marks HTTP header end


print(f"<h1>🙋...ADMIN DASHBOARD / CLIENTS LIST...🙋 </h1><br>")
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
                <td>Email</td>
                <td>Phone</td>
                <td>Is Vip</td>
                <td>Delete</td>
            </tr>   
''')           

for clienT in clients:    
    print(f'''           
            <tr>
                    <td>{clienT.id}</td> 
                    <td>{clienT.name :30}</td>
                    <td>{clienT.email}</td>
                    <td>{clienT.phone}</td>
                    <td>{clienT.is_vip}</td>
                    <td><a href='/web/admin/delete-client.py?id={clienT.id}'a>delete</a></td>
            </tr>
           ''')

print('''</tbody>       
            </table>
                </body>
        
''')


print(
    f"""
    <h1> Add new Client</h1>
    <form action= '/web/admin/add-new-client.py'>
            <input name='name' type='text'placeholder= 'Enter client  name...'/><br>
            <input name='email' type='text'placeholder= 'Enter client email...'/><br>
            <input name='phone' type='text'placeholder= 'Enter client phone...'/><br>
            <input name='is_vip' type='text'placeholder= 'is_vip...'/><br>
            <input name='password' type='password'placeholder= 'enter your password...'/><br>
            <button> ADD NEW CLIENT </button>
    </form> 
    """
)


print(f"<a href='/web/admin/dashboard-prod.py'>GO TO PRODUCTS LIST</a>")

# HW 
# - use the HTML table to show the product stock here 
# - name, q , operations

# - add a link to /web/add-product.py
# - make a from this page which will allow adding new products to stock

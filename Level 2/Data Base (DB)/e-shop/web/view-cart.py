#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
from ast import Index
import sys
import cgi
sys.path.append("/Users/adrian/Desktop/PY-PROJECTS/Level 2/Data Base (DB)/e-shop")

from orm.ProductCatalog import ProductCatalog
from orm.CartManager import CartManager




data = cgi.FieldStorage()

price_sort = data.getvalue('price_sort')


products = ProductCatalog.index(price_sort if price_sort != None else "asc")
bags = CartManager.ViewCart()

# ViewI = CartManager.ViewItem(1)
print("Content-type: text/html; charset=UTF-8") # -> HTTP Heder (encoding for PY to HTML) 
for product in products:    
    pass

print() # \n -> Marks HTTP header end
#body

#print(price_sort)

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View Cart</title>
    <style>
        table, th, td , caption {
          border:1px solid black;
        }
        </style>
</head>
<body>
<h1>🛍...YOUR CART...🛍</h1><br>

    <table>
        <tbody>
            <tr>
                <td>BAG_ID</td>
                <td>BAG_prod_id	</td>
                <td>PROD_prod_id</td>
                <td>NAME</td>
                <td>PRICE</td>
                <td>QUANTITY</td>
                <td>COST</td>
                <td> +1 </td>
                <td>DEL</td>
                <td> -1 </td>
            </tr>   
''')           
# for bagitem in bagitems:
for bag in bags:    
    print(f'''           
            <tr>
                    <td>{bag.bag_id} </td> 
                    <td>{bag.product_id} </td>
                    <td>{product.id} </td>  
                    <td>{product.name :30}</td>
                    <td>{product.price_value}</td>
                    <td>{bag.quantity}</td>
                    <td>{product.quantity * product.price_value}</td>
                    <td><button type="button">add</button></td>
                    <td><button type="button">Del</button></td>
                    <td><button type="button">Rem 1</button></td>
            </tr>   

    ''')
print('''    </tbody>       
        </table>
    </body>
</html>
''')
print(f"<a href='/web/add-to-cart.py?id={product.id}'>Add to: 🛒</a><br>")
print("<h3><a href='/web/catalog.py'> 🍗...PRODUCE CATALOG...🍗 </a></h3>")


# Product List

    # print(f"<h2>{ product.name :30}</h2>")
    # print(f"<p><strong>{product.price_value}</strong>{product.price_unit}</p>")
    # print(f"<p><a href='/web/details.py?id={product.id}'>Details</a></p>")

    
    
#  browser -> text/plain





# HW:
# /view-cart
# * read client_id from cookie Check details.py orentation
# * HINT you could also store cart_id in the cookies
# * make a table on this page
#------------------------------------------------------
#|no  | name  | price | quntity| cost |  operations   |
#------------------------------------------------------
#| 1. | First | 10.0   | 2     | 20   |   +  X  -     |
#------------------------------------------------------


# Product List

    
#  browser -> text/plain
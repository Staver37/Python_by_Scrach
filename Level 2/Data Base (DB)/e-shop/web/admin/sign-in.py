#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
import sys
import cgi
from time import time_ns
from random import randint

import os
# takes the input and puts it into the DATA variable
data = cgi.FieldStorage() # {id: }

sys.path.append("/Users/adrian/Desktop/PY-PROJECTS/Level 2/Data Base (DB)/e-shop")

cookie_data = os.environ.get('HTTP_COOKIE')

# if cookie_data !='':
#     cookie_key, cookie_value = cookie_data.split('=')


#     if cookie_key == 'admin_id':
#         print(f"Refresh: 0; URL=/web/admin/sign-in.py")


# print(f"Refresh: 3; URL=/web/details.py?id={product_id}") # redirecting to details URL
print("Content-type: text/html;charset=UTF-8") # -> HTTP Heder (encoding for PY to HTML) 

print() # \n -> Marks HTTP header end

#print(f"product {product_id}  HAS BEEN ADDED TO THE CART")

print(
    f"""
    <h1> You must sign in to ADMIN PANEL</h1>
    <form>
            <input name='name' type='text'placeholder= 'enter your name...'/><br>
            <input name='password' type='password'placeholder= 'enter your password...'/><br>
            <button> ENTER </button>
    </form> 
    """
)

print(f"<a href='/web/admin/dashboard-prod.py'>GO TO DASHBOARD</a>")

#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
import sys
import cgi
from time import time_ns
from random import randint
import os

sys.path.append("/Users/adrian/Desktop/PY-PROJECTS/Level 2/Data Base (DB)/e-shop")
from orm.Client import *
data = cgi.FieldStorage() # {id: }



cookie_data = os.environ.get('HTTP_COOKIE')

# HW: these verification should be on ALL admin pages
# if admin_id is in the cookies

# if cookie_data !='':
#     cookie_key, cookie_value = cookie_data.split('=')


#     if cookie_key == 'admin_id':
#         print(f"Refresh: 0; URL=/web/admin/sign-in.py")



print("Content-type: text/html;charset=UTF-8") # -> HTTP Heder (encoding for PY to HTML) 
       



id = data.getvalue('id')
name = data.getvalue('name')
email = data.getvalue('email')
phone = data.getvalue('phone')
password = data.getvalue('password')


client = Client(
            id,
            name,
            email,
            phone,
            False,
            password # add hashing
)
client.delete()

print(f"Refresh:0.01; URL=/web/admin/dashboard-client.py")

print() # \n -> Marks HTTP header end

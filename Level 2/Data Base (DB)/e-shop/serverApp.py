#  webserver engines
# http://homepages.math.uic.edu/~jan/mcs275/mcs275notes/lec23.html

#  builtin http web server (pure Python Solution)
from os import system
system("clear")
from http.server import HTTPServer , CGIHTTPRequestHandler
import cgitb; cgitb.enable()
CGIHTTPRequestHandler.cgi_directories = ['/web']

webServer = HTTPServer(("localhost", 8000),CGIHTTPRequestHandler) 

print("starting server...")
webServer.serve_forever()


# static web server
# / < URL  - root directory
# /images/ < URL - images directory 
# /images/1.jpg< URL - images directory



# dynamic content



#      HTTPServer <--------- req
#                 ---------> res
#           v^
#      CGISimpleHTTPRequestHandler
#           v^
#        catalog.py



# CGI - Common Gateway Interface


# HW:
# /view-cart
# * read client_id from cookie 
# * HINT you could also store cart_id in the cookies
# * make a table on this page
#------------------------------------------------------
#|no  | name  | price | quntity| cost |  operations   |
#------------------------------------------------------
#| 1. | First | 10.0   | 2     | 20   |   +  X  -     |
#------------------------------------------------------

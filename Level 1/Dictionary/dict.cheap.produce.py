# Motivation
# 3 diferen Tipes interpreted the data
# Product Data
#  1. separate variable
from os import system
system("clear")

products =[ 
    {"name":"Simple Product","avail":True, "price":100000,},
    {"name":"Complex Product","avail":True, "price":5900,},
    {"name":"Special Product","avail":True, "price":100,},
    {"name":"Non Special Product","avail":True, "price":1,},

]
for i in range(len(products)):
    if products [i]["price"]<100:
        print("The product", products[i]["name"],"ischeap")

print("\n"*1)    
    
    
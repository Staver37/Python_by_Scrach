from http import client
from itertools import product
from os import  system
from unicodedata import name


from orm.CartManager import CartManager
# system("clear")
from orm. Product import Product
from orm.ProductStock import ProductStock
from orm.Client import Client
from orm.Bag import Bag
from orm.BagItem import BagItem
from orm.AuthService import AuthService


#                 AuthService
#   Model  - for Domain ( High level) call           
##############################################################
#      Update  and save Acount
#u_a = Client(2, "Secound  modif name", "Third_Client@g.com " , "+323456789", "f", "aab5138aba")
#AuthService.updateAcount(u_a)

#                Delete Acount by ID
#d_A =Client(4,"x","x","x","x","x") 
#AuthService.deleteAcount(d_A)

#signU =Client (4,"X","Four_Client@g.com","+423456789","t","1234556789")
#AuthService.signUp(signU)
#################################################

#%-----------------V



#                 CartManager
#   Model  - for Domain (High level) call           
##############################################################


# add_B = Bag.create(1,1)
# CartManager.CreateCart(add_B)



        # addItem
add_I = Bag    (6,16611485936407920002)    
add_I = BagItem(6,  2,     1 )
add_I = Product(5,"x","x","x","x","x")
CartManager.addItem(add_I)


      
#                ADD Item in Cart
#         bag_id   prod_id quantity
#              v     v       v
# add_I = BagItem(2,  2,     2 )
# CartManager.addItem(add_I)
      
        # Print by Index
# c_g = CartManager.get(0)
# print(f"Bag:  {c_g.id}")
# print(type(c_g))


          # Print All Clients
# cart = CartManager.ViewCart()
# print(f"{cart}")




#                Remove Item by ID
#R_I =BagItem(2,"x","x") 
#CartManager.removeItem(R_I)

#                Update Item by ID

# u_i = BagItem(1,2,3)  
# CartManager.updateItem(u_i)

##############################################################






#                 ProductStock
#   Model  - for Domain (High level) call           
##############################################################
#                 Is Product Available -> True / False
# available = ProductStock.isProductAvailable(3)
# print(available)


#                add_p Produs

# add_p = Product(6, "Product5 ",50 , "UDS", "1234567890126", 1)
# ProductStock.addProduct(add_p)

        # Create
# c_p = Product(9, "9th name", 900, "USD", "9234567890123", 80)
# c_p.create()


#                Remove Product by ID
# ps_dell =Product(5,"x","0", "0","0",1)
# ProductStock.removeProduct(ps_dell)













#        substract  a Product from the Stock
# p1 = Product(3, "X", "X", "X", "X", 10)
# ProductStock.subProductQuantity(p1)












##############################################################
##############################################################
##############################################################




#           Model  - for orm (low level) call
#                       Product    
#   Model  - for orm (low level) call           
##############################################################
        # Create
# c_p = Product(9, "9th name", 900, "USD", "9234567890123", 80)
# c_p.create()

        #Update and save
# a_p = Product(3, "Third name", 400, "USD", "3234567890123", 30)
# a_p.name = "Third name"
# a_p.save()

        # Dellete 
#d_p = Product(6, "xxx", 000, "xxx", "0000000000000", 00)
#d_p.delete()

        # Print by Index
#g_p = Product.get(2)
#print(f"Product Name:  {g_p.name}, Quantity: {g_p.quantity}, Price Value: {g_p.price_value}")
#print(type(g_p))

        # Print All Products
# all_p = Product.all()
# print(type(all_p))
# print(all_p)
################################################################


#                Client
################################################################
          # Create Client
# c_c = Client(1, "JON", "JON_Client@g.com" , "+1223456789", "f", "12345")
# c_c.create()

          # Print All Clients
# a_c = Client.all()
# print(type(a_c))
# print(f"{id},{name}")
# print(client.name)

#             # Print Client by Index
# g_c = Client.get(16598826654385030004)
# # g_c = Client.get(16575332926176820009)
# print(f"Name: {g_c.name} |  Email:{g_c.email} | Phone :'{g_c.phone}' |  Is_vip:{g_c.is_vip} |  Password:{g_c.password}")
# # print(len(g_c.password))

#     Dellete  Client
# d_c = Client(16611393567521600009, "xxx", 000, "xxx", "0000000000000", 00)
# d_c.delete()
  
#      Alterate and save Client
#a_c = Client(2, "Secound name", "Third_Client@g.com " , "+323456789", "f", "aab5138aba")
#a_c.password = "bababa"
#a_c.save()

################################################################

#                 Bag
################################################################
#       Create Bag
#c_b = Bag(4,1)
#c_b.create()

#      Print All Bags
#a_b = Bag.all()
#print(type(a_b))
#print(f"{a_b}")

#       Print Bag by Index
#g_b = Bag.get(3)
#print(f"Bag ID:{g_b.id}, Client ID: {g_b.client_id}")

#       Dellete  Bag by Index 
#d_b = Bag(4,0)
#d_b.delete()

#       Alterate and save Bag
#a_b = Bag(1,0)
#a_b.client_id = 1
#a_b.save()
################################################################

#                BagItem
################################################################

#       Print Bag Item by Index
#g_bI = BagItem.get(1)
#print(f"Bag ID:{g_bI.bag_id}, Product ID:{g_bI.product_id},  Quantity:{g_bI.quantity} ")

#                    Create BagItem
#            bag_id | product_id | quantity 
#               v        v            v
#c_bI = BagItem(1,        2 ,         2)
#c_bI.create()



#       Alterate and save BagItem
#a_bI = BagItem(2,"x","x")
#a_bI.product_id = 3
#a_bI.quantity = 7
#a_bI.save()

#       Dellete  BagItem by Index 
#             bag_id 
#               v
# d_bI = BagItem(4,2,50)
# d_bI.delete()

#      Print All Bags
#a_b = BagItem.all()
#print(type(a_b))
#print(f"{a_b}")
################################################################








































#from os import system
#import psycopg2

#conn = psycopg2.connect("dbname=e_shop user=postgres ")
#cursor = conn.cursor()
#cursor.execute('SELECT * FROM  "Product";')
#cursor.execute("INSERT  INTO Product(id,name,price_value,price_unit,bar_code,quantity) VALUE (%s,%s)" (5,"fiveth name",500,"USD" , '5234567890123',50))
#conn.commit()

# returns a list of tupless

# HW2 study the tuples / diffs against list
# HW3 try to execute from python all the DOMAIN instruction, try input values from kb

#products = cursor.fetchall()
#system ("clear")
#for product in products:
#    print(product)
     
    

    
   

    





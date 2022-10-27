# HW2
#     - try to finish this class
from http import client
from .BagItem import BagItem
from .Model   import *
from .Bag     import Bag
from .Product import Product

# from .ProductStock import ProductStock

# partial completed
class CartManager:

    def CreateCart(self):
        new_Cart = Bag.create()
        return new_Cart

       
    # complete adding item to cart
    def removeItem(itemID):
        rem_I = BagItem.delete(itemID)
        return rem_I



    def updateItem(id):
        update_I = BagItem.save(id)
        return update_I


    def Clear():
        pass


        
    def ViewCart():
        V_cart = BagItem.all() #<-- mast be get() read cl_id  from cokies
        return V_cart
    

    # def addItem(self):
    #     sql = f"BEGIN;\
    #             INSERT  INTO \"Bag\"     VALUES ({self.id},{self.client_id});\
    #             INSERT  INTO \"BagItem\" VALUES ({self.bag_id},{self.product_id},{self.quantity});\
    #             UPDATE       \"Product\" SET     quantity = quantity - 1 WHERE id = {self.id};\
    #             COMMIT;"
    #     self.executeUpdateSQL(sql)
    #     return sql



    # def addItem(self):
    #     sql = f"BEGIN;\
    #     INSERT  INTO \"Bag\"     VALUES ({self.id},{self.client_id});\
    #     COMMIT;"
    #     self.executeUpdateSQL(sql)
    #     return sql

    def addItem(self):
        sql = f"BEGIN;\
                INSERT  INTO \"Bag\"     VALUES ({self.id},{self.client_id});\
                INSERT  INTO \"BagItem\" VALUES ({self.bag_id},{self.product_id},{self.quantity});\
                UPDATE       \"Product\" SET     quantity = quantity - 1 WHERE id = {self.id};\
                COMMIT;"
        self.executeUpdateSQL(sql)
        return sql






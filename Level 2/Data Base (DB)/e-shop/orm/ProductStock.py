#Model Uper Level (like for real life)

#from typing_extensions import Self
from .Model import Model
from .Product import Product


class ProductStock:

    def isProductAvailable(productId):
        product = Product.get(productId)
        if product == None:
            return False
        elif product.quantity == 0:
            return False
        else:
            return True     




# HW3: finish this metod

        # 1. check if the product exist in the table (doesnt work isProductAvailable)
        # 2. if it doest exist -> product.create()
        # 3. if it exist? -> sum some quantity
    # FINISHED

    def addProduct(self):# Create new prod if not exist
        product = Product.get(self.id)                                                                                     
        if product == None:    
            createProd = Product.create(self)
            return createProd
        else: # if it exist? -> sum some quantity
            sql = f"UPDATE \"Product\" SET quantity \
                = quantity + {self.quantity} WHERE id = {product.id};"
            self.executeUpdateSQL(sql)
            return sql
            


# HW4: finish the method that removes the product complectly
    def removeProduct(productId):
        Product.delete(productId)

# HW5: finish the method that substract  a product quantity from stock prodbuct
    # - verifica daca este drodus in stock
    # - Update the quantity  
    # - Save
    


    def  subProductQuantity(self):
        Sprod = ProductStock.isProductAvailable(self)
        return Sprod
   
        

import psycopg2
from .Model import Model

class Product(Model):
    def __init__(

        self,
            id,
            name,
            price_value,
            price_unit,
            bar_code,
            quantity
    ):

            self.id = id                    
            self.name = name
            self.price_value = price_value
            self.price_unit = price_unit
            self.bar_code = bar_code
            self.quantity = quantity
   

   
    def delete(self):
       sql = (f"DELETE  FROM \"Product\" WHERE  id = {self.id};")
       self.executeUpdateSQL(sql)
       

    def all(price_sort):    
        sql = f"SELECT * FROM \"Product\" ORDER BY price_value {price_sort};"
        products_list = Product.executeFetchSQL(sql)
        products = []
        for product_tuple in products_list:
            #HW 1: try to optimize multiple parameters intro function
            product = Product(*product_tuple)
            products.append(product)
        return  products    


 

    def get(id):    
        sql = f"SELECT * FROM \"Product\" WHERE id = {id};"       
        product_l = Product.executeFetchSQL(sql)
        if len(product_l) > 0:       
            product_tuple = product_l[0] # to optain ressult
            product = Product(*product_tuple)
            return  product      
        else:
            return None


    def create(self):
       sql=(f"INSERT  INTO \"Product\"VALUES ({self.id},'{self.name}'\
            ,'{self.price_value}','{self.price_unit}','{self.bar_code}',\
             {self.quantity});")
       self.executeUpdateSQL(sql)


    def save(self):
       sql = f"UPDATE \"Product\" SET name = '{self.name}', price_value = {self.price_value},\
         price_unit = '{self.price_unit}', bar_code = '{self.bar_code}', quantity = {self.quantity} WHERE id = {self.id} ;"
       self.executeUpdateSQL(sql)


    def __str__(self):
       return f"Prooduct id{self.id}"

    def __repr__(self):
         return str(self)  


    # HW2:  complete the code for the models : Bag, BagItem, Client    

    #   OOP inheritance
    
    
    #     Model
    #      v
    #   Product
    #   Client
    #   Bag
    #   BagItem
from os import system
system("clear")

# declare the class 
class Product:    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def  printIt(p): 
         print("Product:", p.name, p.price)

# create some objects
p1 = Product("OS",100)   
p2 = Product("Antivirus",50)
p3 = Product("Game",10)

##################################
Product.printIt(p1)
Product.printIt(p2)
Product.printIt(p3)
##################################


print("\n"*5)
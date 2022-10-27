# advanced errors
from os import system
from tkinter.messagebox import YES
system("clear")

product_name = "Sare"
product_price = 100000
delivery_cost = 5

print("#################################")
print(product_name,":",product_price,"$/kg")

answer = input("Vreti sa cumparati? ")
#HW1 Update the condition
#        "yes", "y"
#        "YES", "Y"
if answer == "da":
    
    order_quantity = int (input("Cit doriti?"))
    order_cost = order_quantity * product_price
    print("-------------------------------------")
    print("Order Info")
    print(product_name, "x" , order_quantity,"=",order_cost)

    answer= input("Doriti livrare ?")
    if answer == "da":
        order_cost += delivery_cost
        print("order cost(including delivery)",    order_cost)
        print("################################")
        if answer == "nu":
             print("No Problem you can pick up from store")
             print("##################################")        
else:
    print("Foarte rau, o sa mincati nesarat :(")
    print("################################")
    print(" Te iubesc, E mai sanatos fara sare si mai eftin *)")
    


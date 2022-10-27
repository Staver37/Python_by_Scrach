from os import system
system("clear")
print("\n"*5) 

# DATA SOURCE
# list > dict
data = [ # level 0
    {
        "title":   "Salad",  # level 1
        "price":   {
        "amount" : 15.00,
        "currency" : "MDL" 
        },
        "quantity": 2   
    },
    {
        "title": "Soup",
        "price":{
        "amount" :  40,
        "currency" : "MDL" 
        },
        "quantity": 1
    },
    {
        "title": "Bread",
        "price":{
        "amount" :  2.50,
        "currency" : "MDL"
        },
        "quantity": 10
    },
]
# PRINT / ITERATE
for i in range (len(data)):
    item = data[i]
    
    item_cost = item["quantity"] *  item["price"]["amount"]
    item_currency = item["price"]["currency"]
    
    out = f'{i+1:2}) {item["title"]:^15} x {item["quantity"]:3}  = {item_cost: 8.2f} {item_currency}'
    print(out)
    
print("\n"*5)    
 
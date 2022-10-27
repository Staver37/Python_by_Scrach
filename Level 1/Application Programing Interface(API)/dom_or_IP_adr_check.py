from os import system
from trace import Trace
system("clear")
import requests

# HW 1 make it interactive
while True:
    system("clear")
    
    print("MAIN MENU")
    print("Press 1 FOR CHEKING Domanian or  IP adress: ")    
    print("Press 0 EXIT") 
    i = int(input(">>>>>"))
    
    
        
    
    while True:    
        if i == 1:
            system("clear")
            query = input("Enter a domanian or IP adress :   ")
            url = f"http://ip-api.com/json/{query}"
            res = requests.get(url)
            data = res.json()
        if data['status'] == 'success':
                #print(type(data))
                #print(data)
                print(data['country'] )
                print(data['regionName'])
                print(data['isp'])
                input("\nHit ENTER to continue")         
       
        else:
            
            print("Not found!")
            print("\n"*2)

        if i == 0:
            break
            
                       
            
            
            
        
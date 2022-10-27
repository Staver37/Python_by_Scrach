from os import system
import datetime
today = datetime.datetime.today()
system("clear")
import requests
###############################

date = f"{today:%d.%m.%Y}"
url = f"https://www.bnm.md/en/export-official-exchange-rates?date={date}"

res = requests.get(url)
data = res.text

lines = data.split("\r\n") # str.split() -> list[]
usd_rate =  0.0
eur_rate = 0.0
mdl_rate = 0.0

#print(data)
#print(lines)

for l in lines [3:-5]:
    currency = l.split(";")
    if currency[2] == 'USD':
        usd_rate =float( currency[4].replace(",",".") )
    if currency[2] == 'EUR':
        eur_rate =float( currency[4].replace(",",".") )
    if currency[2] == 'MDL':
        eur_rate =float( currency[4].replace(",",".") )
    
    #print(currency)
while True:
    system("clear")
    print("   ",date)
    print("CHOSE THE CURENCY:""\n")
    print("  USD:")
    print("  EUR:")
    print("  MDL:  ""\n")
    
    c1 =        input("I have: >>> ")
    c2 =        input("I Want: >>> ")
    amount =int(input("Amount: >>> ") )
    print(" \n")
        # USD  -> MDL
    if c1 == "USD" and c2 == "MDL":
        r = usd_rate * amount
        print(f" >>> " ,r,"LEI" "\n" )
        
        # MDL -> USD
    if c1 == "MDL" and c2 == "USD":
        r = amount / usd_rate
        print(" >>> " ,r ,"$" "\n" )  
        # EUR -> MDL
    if c1 == "EUR" and c2 == "MDL":
            r = eur_rate * amount
            print(" >>> " ,r ,"LEI" "\n" ) 
        # MDL -> EUR
    if c1 == "MDL" and c2 == "EUR":
            r = amount / eur_rate 
            
            print(" >>> " ,r ,"EUR" "\n" ) 
        # USD -> EUR
    if c1 == "USD" and c2 == "EUR":
            r = (amount * usd_rate) / eur_rate
            print(" >>> " ,r ,"EUR" "\n" )
      
        # EUR -> USD
    if c1 == "EUR" and c2 == "USD":
            r = (amount * eur_rate) / usd_rate
            print(" >>> " ,r ,"$" "\n" )  
    
    input(" HIT ENTER FOR CONTINUE")
    
    
    
# HW     add interactivity
#        chose source curency USD/EUR/MDL
#        input amount < user
#        chose destination currency USD/EUR/MDL
#        output amount > user

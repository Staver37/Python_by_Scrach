##  user --> amount money --> CONVERTER --> display

#HW1 - Finish 2 cases (combination)
#    - make the MENU more logical
#    - built in python functions - round

print("################################")
print("SELECT INPUT CURRENCY")
print(" * EUR")
print(" * USD")
print(" * MDL")
print("################################")
currency_in = input("chose:")
money_in    = float(input("money:"))

print("################################")
print("SELECT OUTPUT CURRENCY")

if currency_in != "EUR":
    print(" * EUR")

if currency_in != "USD":
    print(" * USD")

if currency_in != "MDL":
    print(" * MDL")

print("################################")

currency_out =input("chose:")
eur_2_usd    = 1.10
eur_2_mdl    =20.21
usd_2_mdl    =18.39

if currency_in == "EUR" and currency_out == "USD":
   money_out    = money_in * eur_2_usd 
if currency_in == "USD" and currency_out == "EUR":   
    money_out   = money_in / eur_2_usd

if currency_in == "EUR" and currency_out == "MDL":
   money_out    = money_in * eur_2_mdl 
if currency_in == "MDL" and currency_out == "EUR":   
    money_out   = money_in / eur_2_mdl

if currency_in == "USD" and currency_out == "MDL":
   money_out    = money_in * usd_2_mdl 
if currency_in == "MDL" and currency_out == "USD":   
    money_out   = money_in / usd_2_mdl

money_out=round(money_out ,2 )
print(money_out)
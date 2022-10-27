#HW money calculator
# money calculator

#INS:

# * amount of money $
# * bills (1,5,20)
# OUT
# * number of bill

money = int ( input("Enter $: ") ) 

bills_20 = money // 20 

bills_5 = money // 5 % bills_20

bills_1 = money % 5


print (bills_20, "x20+" , bills_5, "x $5" , bills_1, "x $1" )
 

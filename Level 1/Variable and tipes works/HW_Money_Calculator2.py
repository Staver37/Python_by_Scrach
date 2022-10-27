#HW money calculator
# money calculator

#INS:

# * amount of money $
# * bills (1,5,20)
# OUT
# * number of bill

money = int ( input("Enter $: ") ) 

bills_20 = money // 20 
bills_20_1 = bills_20 * 20

bills_5_1 = money - bills_20_1
bills_5_2 = bills_5_1 // 5
bills_5_3= bills_5_2 * 5

bills_1 = money - bills_5_3 - bills_20_1

print (bills_20, "x20+", bills_5_2, "x $5" , bills_1, "x $1" )
 

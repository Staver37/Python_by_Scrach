# money calculator

#INS:

# * amount of money $
# * bills (1,5)
# OUT
# * number of bill
# 7 -> 1 x $5 + 2 x $1
# 10 -> 2 x $5  + 1 x $1


# HW1:
# what if bills 1,5,20)


money = int ( input("Enter $: ") )

bills_5 = money // 5
bills_1 = money % 5
# bills_1 =money - bills_5 * 5

print ( bills_5, "x $5 +", bills_1,"x $1" )
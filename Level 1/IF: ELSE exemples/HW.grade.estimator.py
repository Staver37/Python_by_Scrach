# IN : stutent's grade 1..10
# Out : good, ok, bad

# x--------->x-------->x------>x
# 1         4         7      10

grade= int(input("Your grade:    "))

if grade > 7 and grade <= 10:
    print("GOOD!")
elif grade > 4 and grade <= 7:
    print("OK!")
elif grade >= 1 and grade <= 4:
    print("BAD!")
        
# WH1 : continue with  - WRONG VALUE 
else:
    print("WRONG VALUE!")
    
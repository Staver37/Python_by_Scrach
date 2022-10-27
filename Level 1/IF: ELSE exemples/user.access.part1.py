#IN: login, pass
#FACT:
#OUT:  message

# from database
SYS_LOGIN= "admin" #  str
SYS_PASSW = "1234"  # str

# from user input
login       = input("login:  ")
passw       = input("pass:  ")

# logic
hasAccess = SYS_LOGIN == login and SYS_PASSW == passw

if hasAccess: # == True(in py var access automat este de tip bool are incorporat T/F)
    print("Access grated!")
else:
    print("Access DENIED!")
    
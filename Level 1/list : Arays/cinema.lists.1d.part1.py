from os import system
#   LEGEND
# 0 - FREE
# 1 - RESERVED
# 2 - BOUGHT
seats = [0, 0, 0, 0, 0, 0, 0, 0 ]
#index   0, 1, 2, 3...........7

option = -1
while option != 0:
    # #####iterative count algoritm #####
    # HW1 : let's say free_seats = len (seats)
    # free_seats = 0
    free_seats = len (seats) 
    for pi in range (len(seats)):
        if seats[pi] == 0:
            free_seats += 1
            
# ###################################

    # ########## PLOT ###################
    
    system("clear")
    print()
    for pi in range ( len(seats)):
        print("",pi+1,"",end="  ")
    print()   
    for pi in range ( len(seats) ):
        if seats[pi] == 1:
            print("|-|",end="  ") 
        elif seats[pi] == 2:    
            print("|+|",end="  ")
        elif seats[pi] == 3:
            free_seats += 1    
            print("| |",end="  ")
        else:
            print("| |",end="  ")
    print("\nFREE SEATS:", free_seats - 8)
    print("\n")
    # ########## PLOT ###################
    # ######## show MENU ################
    print("MENU")
    print("1. Book")
    print("2. Buy")
    print("3. Cancel")
    print("0. Exit")
    print("----------------------------------------")
# ################1###########################
    
    option = int(input("Meniu Option >>>"))
    # HW 2: add check condition:
    #       - boundaries
    #       - check if the place is free
    # HW 3: add buy, cancel
          
    # book
    if option == 1:
        place = int(input("Wich place?>>>"))
        if place in range(0,9):
           seats[ place - 1 ] = 1
    # Buy
    if option == 2:
        place = int(input("Wich place?>>>"))
        if place in range(0,9):
           seats[ place - 1 ] = 2     
         
    # Cancel 
    if option == 3:
        place = int(input("Wich place?>>>"))
        if place in range(0,9):
          seats[ place -1 ] = 3       
    print("")
    
        
       
           
    # ##### HW3: add buy, cancel ###########    
    
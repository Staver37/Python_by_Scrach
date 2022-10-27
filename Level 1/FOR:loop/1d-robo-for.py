# REMAKE 1d robo game -> for loop
from os import system
roboX  = 5
roboHP = 100
bombX1 = 7
bombX2  = 2
heart   = 10
roboBT = 100
coin1   = 22
score = 0 



LENGHT = 20

option=""
# game loop
while True:
    system("clear")
    ##############Draw Map################
    print("\n")

    for x in range (1, LENGHT + 1):  #1....10
        if x == roboX:
            print("⛄", end=" ")
        elif x == bombX1:
            print("💣",end=" ")
        ###################
        
        elif x == bombX1:
             print(".",end=" ") 
        
        ###################
        elif x == bombX2:
            print("💣",end=" ")
        elif x == heart:
            print("💟",end=" ")
        elif x == coin1:
            print("💰",end=" ")         
        else:
            print (".",end=" ")
    print("\nHP:" , roboHP )
    print("BT:",roboBT,"%")
    print("SC:",score)
    print("\n")   
##############1.Draw Map#################
##############2.Read Input################  
    option=input(">>>")   
##############2.Read Input################  
##############2.Read Input################
##############3. DECIDE ##################
    #HW1 ##############
    if option == "a" and roboX > 1 :     # move left
        roboX  -= 1 
        roboBT -= 1
    if option == "d" and roboX < 6:     # move right
        roboX +=1
        roboBT -= 1
        #HW1 ##############
        
# check if bomb   
    if roboX == bombX1:
        roboHP -= 10 
        
    if roboX == bombX2:
        roboHP -= 10 
        print(". ")
       
# check heart        
    if roboX == heart:
        roboHP += 30
# check score        
    if roboX == coin1:
        score += 10    
        #HW2 ###############
        if roboHP <=1:
            print("GAME OVER")
            break 
        # HW2 ##############
    if option == "x": # aeXit
        system("clear")
        print ("Thank you for playing!")
        print("\n") 
        break
###############3. DECIDE #################
     
# HW1 : frontier check right     *       
# HW2 : Game over if  HP         *
# HW3 : place secoun bomb        * 
# HW4 : place some hearts        * 
# HW5 : place some coin -> score *
# HW6* : add variables  add variables -> state of bombs , coins,....  
   
   
   
   #     game loop:
   #   1. draw the map
   #   2. read the input
   #   3. decide
   
   
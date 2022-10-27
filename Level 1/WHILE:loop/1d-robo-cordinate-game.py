# STEP 3
# -----R----->
#CONTROLS : "a" - left, "d" - right
from os import system
from this import d

LENGHT = 100

roboX  = 5

direction = ""

# game loop
while direction != "x":
    system("clear")
    # ########### DRAW THE MAP ############
    print ("\n") # + "\n"
    x = 1
    while x <= LENGHT:
        if x == roboX:
            print("R" ,end="") #"\n"
        else:
            print("-" , end="") #"\n"
        
        x += 1
        
    print("\n") #+"\n"
    # ########### DRAW THE MAP ############
        
    # ########### CONTROLS     ############
    direction = input("dir(a/d) >>>")
    if direction == "a":
        roboX -= 1
    if direction == "d":
        roboX +=1    
    # ########### CONTROLS     ############

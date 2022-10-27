#     * * * * * * * * * * *
#     * * * * * * * * * * *
#     * * * * * * * * * * *
#     * * * * * * * * * * *
#     * * * * * * * * * * *
#     * * * * * ^ * * * * *
#     * * * * * * * * * * *
#     * * * * * * * * * * *
#     * * * * * * * * * * *
#     * * * * < R > * * * *
from os import system
from time import sleep
from random import randint
# robot cords
score = 0
rx = 5
# bullet cords / -1 not active
bx = -1
by = -1
# target cords 
tx = 5
ty = 3





option = ""
while option !='x':

    
    ############### DRAW THE MAP ############
    system ("clear")
    for y in range(1,11):
        for x in range(1,11):
            if x == rx and y == 10:
                print("R", end=" ")
            
            elif x == bx and y == by:
                print("^", end=" ") 
            
            elif x == tx and y == ty:
                print("X", end=" ") 
             
            else:    
                print(".", end=" ")
        print()
    sleep (0.02)    
    #########################################
    
    ################### BULLET ###############
    if by != -1:
        by -= 1
    # HW1: add score variable
    #      increment when hiting a target                
        if tx == bx and ty <= by:
            score += 1
        
        if bx == tx and by == ty:
          ty = randint (1,7)
          tx = randint (1,10)
        
        continue
    ####################CONTROL##############
    print("Score:", score)
    
    print('\n')
    option = input(">>>")
    if option == 'a':
        rx -= 1
    if option == 'd':
        rx += 1 
    if option == ' ':
        bx = rx     
        by = 10 - 1
    
    #########################################
        ######################################
    
    
   
    
    
    
    
    
    
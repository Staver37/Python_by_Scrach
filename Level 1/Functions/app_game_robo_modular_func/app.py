from map import *
from ui import *

while True:
    clear()
    printMap(gameMap)
    key =controls()
    
    gameMap[rr][rc] = 0    # earse the robot
    if key == 'x':
        break
    # Moove Right
    ####################
    if key == 'd' and gameMap[rr][rc+1]!=1:
        rr == [8]
        rc += 1             #increment coord R  
    ####################
    #  # Moove Left  
    if key == 'a' and gameMap[rr][rc-1]!=1:
        rc >= 10
        rc -= 1             #increment coord R
     # Moove UP
    if key == 's' and gameMap[rr+1][rc]!=1:
       rr += 1              #increment coord R
   # Moove Down
    if key == 'w' and gameMap[rr-1][rc]!=1:
        rr -= 1             #increment coord R
    gameMap[rr][rc] = 2     # put the robot in coord
    
    # HW1 : add UP/Down +
    # HW2 : bourdaries check right 9 left - 0
    # HW3*: add some mines,+
    #       when muving right -> radar rc+1,rc+2 -noT A MINE -
    #       in case of danger -> WARNING -> danger detected  -  
    
#            . . . . X . . . . . 
#            # # # # # . . . . . 
#            . . X . . . . . . . 
#            . . . . . . . . . # 
#            . R . X # # # . . # 
#            . . . . . # . . . # 
#            # # # # . # . . . . 
#            . . . . . # . . . . 
#            . . X . . # . . . # 
#            . . . . . . . . . # 

        
## THE WALKING GAME

## - functions
## - modules
## - events
## - loops
## - conditionals
## -operations
#import turtle as t
# map size W xH (pixels)
#--------x----------->
#|
#|
#y
#|
#|
#|
#v
from lib import *

windowSetup()
showMario(marrioX,0)
showCoin(coinX)
# ##########
RCP()
showCoin(coinX)
# ##########
# KEY biding

t.listen()
t.onkey(moveRight, 'Right')
t.onkey(moveLeft, 'Left')
t.mainloop()

 
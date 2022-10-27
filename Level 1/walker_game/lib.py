from cgitb import reset
from distutils.command.clean import clean
from tkinter.ttk import Style
import turtle as t
from turtle import Turtle
from random import randint
from os import system 

# WINDOW SETUP

marrioFrame = 1
marrioX = 0
marrioDir = 'r'
marrioScore = 0

coinX = randint(-400,400)

# create two separate pens
t_marrio = Turtle()
t_coin   = Turtle()

#######################
def moveRight():
   
    global marrioX
    global marrioFrame
    global marrioDir
    global marrioScore
   
    marrioX += 50
    marrioFrame += 1
    if marrioFrame == 5:
        marrioFrame = 1
        
    marrioDir = 'r'    
    showMario(marrioX,0)
    #if marrioX -20 <= coinX and marrioX + 20 >= coinX:
    if coinX in range(marrioX -20 , marrioX + 20 ):
        print(marrioScore)
        marrioScore += 10  
 #HW1 clear the screen ###########       
    print(marrioScore)
    t.clear()   
    showScore()
 #HW1 clear the screen#############   
    
    #
    #          coinX299
    #x---------|-^v--|--------------->
    #          marrioX
    #
    #
    
def moveLeft():
    global marrioX
    global marrioFrame
    global marrioDir
    global marrioScore
    marrioX -= 50
    marrioFrame += 1
    if marrioFrame == 5:
        marrioFrame = 1
    marrioDir = 'l'    
    showMario(marrioX,0)
    if coinX in range(marrioX-20,marrioX+20):
        print(marrioScore)
        marrioScore += 10    
    #HW1 clear the scree
    t.clear()   
    print(marrioScore)
    showScore()
    #HW1 clear the screen
       
     
#HW2
def showScore():
    global marrioScore
    t.penup()
    t.setposition(0,-200)
    t.pendown()
    Style = ('Courier', 40 ,'bold')
    t.write(f'{marrioScore}',font = Style)
    
def windowSetup():
       
    WIDTH   =  1000
    HEIGHTS =  400
    t.setup(WIDTH , HEIGHTS)
    t.showturtle()
    
# DISPLAY AN IMAGE COIN
def showCoin(x):
    global t_coin

    name =f'images/coin.gif'
    s = t.Screen()
    s.addshape(name)
    t_coin.penup()
    t_coin.setposition(x,0)
    t_coin.shape(name)

    
# DISPLAY THE MAIN CHARACTER

def showMario(x,y):
    global marrioFrame
    global marrioDir
    global t_marrio
    name =f'images/marion-{marrioDir}-{marrioFrame}.gif'
    s = t.Screen()
    s.addshape(name)
    t_marrio.penup()
    t_marrio.setposition(x,y)
    t_marrio.pendown()
    t_marrio.shape(name)
    
    #HW2-----------------------------------------------

def RCP(): #Reset random coin pozition
    global t_coin
    global coinX
    
    if marrioX in range (coinX - 20 , coinX + 20 ):
        t_coin.clear()  
        
    # --------------------------------------------------
    #HW1 clear the screen
    #HW2 each the Mariio gets  the coin ++ set a new random X to the coin

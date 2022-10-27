#clock module
from os import system
system("clear")
from ast import arg
from cgitb import grey
import turtle as t
from xml.etree.ElementPath import get_parent_map
# time data
hours = 12
minutes = 15
seconds = 50

#print the time
def printTime():
    print (f"{hours:02}:{minutes:02}:{seconds:02}" )    # template strings

# draw clock with turtle
def drawClock():
    t.speed(0)
    t.pensize (3)
    t.color("brown")
    t.circle(100)
    t.penup()
    t.goto(0,95)
    t.pendown()
    t.circle(5)
    t.penup() 
    t.goto(0,130)
    t.color("blue")
    t.write( arg= "KROLEX:)", move=False, align='center' , font= 'caveat' )
    t.goto(0,0)
    t.color("black")
    t.write( arg= "6" , move=False, align='center' , font= ('Arial',25))
    t.penup()
    t.goto(0,170)
    t.write( arg= "12" , move=False, align='center' , font= ('Arial',25))
    t.goto(-90,85)
    t.write( arg= "9" , move=False, align='center' , font= ('Arial',25))
    t.goto(90,85)
    t.write( arg= "3" , move=False, align='center' , font= ('Arial',25))
    t.goto(0,0)
    t.left(90)
    t.penup()
    t.forward(100)
    
    # hours indicator
def indicactorH():    
    t.pendown()
    t.pensize (3)
    t.color("red")
    t.right(hours*30)
    t.forward(70)
    
    # reset the pen
    t.penup()
    t.left(180)
    t.forward(70)
    t.right(180-hours*30)
 
    
    #minutes indicator
def indicatorM():    
    t.pendown()
    t.pensize (2)
    t.color("green")
    t.right(minutes * 6)
    t.forward(95)
    
    # reset the pen
    t.penup()
    t.left(180)
    t.forward(95)
    t.right(180- minutes * 6) 
    
    # secounds indicator
def indicatorS():   
    t.pendown()
    t.pensize (1)
    t.color("blue")
    t.right(seconds * 6)
    t.forward(98) 
 
    # reset the pen
    t.penup()
    t.left(180)
    t.forward(95)
    t.right(180 - minutes * 6)        
     
    # HW1 : continue drawing the seconds indicator
    #  *     try another color for it
    # HW2*: try another way of drawing
    # HW3*: try to make 4 different functions
     
    input("hit enter to exit")
    
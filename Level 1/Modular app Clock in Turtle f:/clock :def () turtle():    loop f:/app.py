## main application module
from clock import * 
from time import sleep
from os import system
from datetime import datetime

while True:
    sleep(1)
    d = datetime.now()
    seconds = d.second
    system("clear")
    printTime (d.hour , d.minute , d.second )
    CheckAlarm()  
    drawClock( d.hour,  d.minute , d.second )
   

from os import system
from time import sleep
# ad content
ads = [
    "Buy this Python book for only 0.99",        # 0
    "Try this course of Python for free!!!",     # 1  
    "Drink a lot of water (2L per day minimum)"  # 2  
]
ads_duration = [
    1.0,
    3.0,
    5.0
]
# Method 1 : index only
'''
index =0
while True:
    system("clear")
    print(">>",ads[index],"<<")
    sleep(2)
    index +=1    
    if index >= len(ads):
       index = 0
'''        

# Method 2 methods only
'''
while True:
    ad = ads.pop(0)
    system("clear")
    print(">>", ad,"<<")
    sleep(3)
    ads.append(ad)
'''
# HW1 apply the corect duration from - ads_duration 
while True:
    system("clear")
    print(">>", ads[0],"<<")
    sleep(ads_duration[0])
    system("clear")
    print(">>", ads[1],"<<")
    sleep(ads_duration[1])
    system("clear")
    print(">>", ads[2],"<<")
    sleep(ads_duration[2]) 
from os import system

def clear():
    system("clear")
    
def controls():
    print("use a,d,s,w - for movement")
    key = input(">>>")
    return key

def printW():
    print("WARNING,    BOMB!")
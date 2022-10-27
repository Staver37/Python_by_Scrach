from os import system
system("clear")
file =  open("name.txt","r")
name = file.read()
file.close()
print(name)

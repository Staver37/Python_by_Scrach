name = input("Enter your name plese:") # user input Console > str
file = open("name.txt","w" )# w - write
file.write(name)
file.close()
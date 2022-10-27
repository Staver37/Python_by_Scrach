from os import system
system("clear")
# Input (kb) >> struct Output(console)
# template dict

person = {
    "Full Name" : "Enter your full name",
    "City"     :  "Where do you live?  ",
    "Street"  :   "What street         " 
} 

#INPUT data
for key in person:
    person[key] = input(person[key] + ": ")
print("\n")    
# OUTPUT data
for key in person:
    print(f"{key:>15}: {person[key]:20}")
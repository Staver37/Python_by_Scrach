# FACT: list of friends

# empty lists
friends = []
while len ( friends ) < 100:
    name = input("Add friend name: ")
    if name == " ":
        break
# ### HW 1 : check if the name is in the list ####################  
    if name in friends:
        print(">>>>>>>>  Atention!!!      Duplicate<<<<<<<<<<  ")
# ################################################################        
    friends.append( name )
    
print("You have" , len( friends ), "friends" )
for i in range ( len(friends)):
    print("   ",i,">>>>>", friends[i])
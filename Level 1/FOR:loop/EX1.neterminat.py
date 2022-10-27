
print("\n")

for x in range(1,11):    
    for y in range(1,11):
        
        if x == 1:
            print("1", end=" ") 
        
        if x == 10:
            print("4", end=" ")
            
        if y == 1:
            print("2", end=" ")
        
        if y == 10:
            print("3", end=" ")
        
        else:
            print(".", end=" ")        
    print(" ")
print("\n")
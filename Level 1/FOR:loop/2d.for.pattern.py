#     * * * * * * * * * * *
#     * * * * * * * * * * *
#     * * * * * * * * * * *
#     * * * * + + + * * * *
#     * * * * + R + * * * *
#     * * * * + + + * * * *
#     * * * * * * * * * * *
#     * * * * * * * * * * *
#     * * * * * * * * * * *
#     * * * * * * * * * * *
rx = input ("X >>>")
ry =input("Y >>>")
print()

for y in range(1,11):
    
    for x in range (1,11):
        if x == rx and y == ry:
            print("R", end=" ")
        
         # Top border
        
        elif x == rx - 1 and y == ry - 1:
            print("+", end=" ")
        elif x == rx and y == ry - 1:
            print("+", end=" ")    
        elif x == rx + 1 and y == ry - 1:
            print("+", end=" ")    
       
        # Left / Right borders
        
        elif x == rx - 1 and y == ry :
            print("+", end=" ") 
        elif x == rx + 1 and y == ry :
            print("+", end=" ")  
        
        # Below borders
        
        elif x == rx - 1 and y == ry + 1:
            print("+", end=" ")      
        elif x == rx and y == ry + 1:
            print("+", end=" ")          
        elif x == rx + 1 and y == ry + 1:
            print("+", end=" ") 
            
        else:
            print(".", end=" ")    
    print()
    
print()            
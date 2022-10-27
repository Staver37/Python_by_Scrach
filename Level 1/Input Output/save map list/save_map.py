gameMap =[
    [2,0,1],
    [0,2,1],
    [3,0,3],
]
coord = [6]


# ALGO -> save the map
# manual serialization
def saveMap( m,c ):
    file = open("map.txt","w")
    for ri in range(3):
        for ci in range(3):
            file.write(str(m[ri][ci]))
    
    file.write(str(c))
    file.close()

# ALGO > load map from file


def loadMap(m, c ):
    file = open("map.txt","r")
    
    for ri in range(3):
        for ci in range(3):
            m[ri][ci] = int(file.read(1)) # str -> int
    
    c[0] = int(file.read(1))
    file.close()

def printMap( m, c ):
   
    for ri in range(3):
        for ci in range(3):
            print(str(m[ri][ci]),end=" ")
        
        
        print()
         
    print(c[0])    
    

######################
saveMap(gameMap,coord)
printMap(gameMap,coord)
#loadMap(gameMap,coord)       
  
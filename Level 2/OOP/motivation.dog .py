
# REAL WORLD STRUCTURE (dog)---> code


# A. PRIMITIVE++ WAY

# 2. actions
def dog_bark():
    print("Whooooof Whooooof!")
    
def dog_eat(food_kg):
    if food_kg >= 1:
        print("Whooooooooooooooooof")
    else:
        print("Rrrrrrrrrrrr!!!")
        

        
# 1. proprieties
dog = {
    "name"  : "Tuzik",
    "year"  : 2010,
    "race"  : "Bulldog",
    "alive" : True,
    "eat"   : dog_eat,  
    "bark"  : dog_bark
}
print(dog['name'])
if dog['alive']:
  print("Yeeey")
dog["bark"]()
dog["eat"](0.100)


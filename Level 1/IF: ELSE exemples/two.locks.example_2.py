# exemple for two dors 
# first dor in building
# second dor is in flat


PIN_DOOR_1 = "0123" # Building door
PIN_DOOR_2 = "4321" # Flat Door

#user input
pin_dor_1 = input("Enter first pin:")
lock_1_open = pin_dor_1 == PIN_DOOR_1

if lock_1_open:
    print("I,m in the BUILDING")
    
    pin_door_2 =input("Enter second pin: ")
    lock_2_open = pin_door_2 == PIN_DOOR_2 
    
    if lock_2_open:
        print("I'm in the FLAT")
    else:
        print("WRRONG PIN: ACCES DENIDE IN THE FLAT  ")
else:
    print("WRRONG PIN: ACCES DENIDE IN THE BUILDING  ")  


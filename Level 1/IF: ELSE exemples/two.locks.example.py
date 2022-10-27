PIN_DOOR_1 = "0123"
PIN_DOOR_2 = "4321"


#user input
pin_dor_1 = input("Enter first pin:")
pin_dor_2 = input("Enter second pin:")


lock_1_open = pin_dor_1 == PIN_DOOR_1 # bool
lock_2_open = pin_dor_2 == PIN_DOOR_2# bool



if lock_1_open and lock_2_open:
    print("I'm in the flat")
else:
    print("WRRONG PIN: ACCES DENIDE  ")

#HW : add Else mesage
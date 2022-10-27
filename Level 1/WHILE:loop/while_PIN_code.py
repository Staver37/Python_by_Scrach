# give the user 3 tries enter pin code
SECRET_PIN = "1234"
tries      = 0

while tries < 3:
    # ########## enter and verify 1 time #######
    input_pin = input("PIN:   ")
    if input_pin == SECRET_PIN:
        print("Access grated!!!")
        tries = 1000
    else:
        print("Access  denited!!!")
    tries += 1
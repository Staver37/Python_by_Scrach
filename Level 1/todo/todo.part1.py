# typical exemple
# APP -> memory ->task
# CRUD / BREAD
from os import system
tasks = [] # empty lists
# MAIN LOOP  ######################################
while True:
    system("clear")
    print("MENU")
    print("1. add tasks")    
    print("2. show tasks")
    print("3. remove task")
    print("4. change task")
    print("5. Swap task A with Task B")
    print("0. Exit")
    option = int(input(">>"))
    if option == 1:
        system("clear")
# Add TASKS ######################################
        while True:
            new_task = input("Name you next task: ")
            if new_task == "":
                break
            if new_task not in tasks:
                tasks.append( new_task )
# PRINT TASKS ######################################
    if option == 2:
        system("clear")
        print("\nYour tasks: ")

        for i in range(len(tasks)):
            print(i+1,">>>>>",tasks[i])
        input("\nHit ENTER to continue")

# REMOVE A TASK ####################################       
# HW1  p 3 ask for the index -> remove / python list metods
#     * print the task title / confirm yes/no ? 
    
    if option == 3:
        system("clear")
        while True:
            index = int(input("Enter task position you want remove :"))-1
            print(tasks[index])
            i = input("Type YES to remove this TASK:") 
            if i == "0":
                break
            if i == "YES":
                tasks.pop(index)      
# EDIT A TASK ####################################       
    if option == 4:    
        system("clear")
        index = int(input("Enter task position:"))-1
        new_task = input("Enter edited task: ")
        tasks[index] = new_task

# HW 2 +p 5 swap taskA with taskB -> indexA, indexB
    if option == 5:
        system("clear")
        i1 =int(input("Enter Task A: "))
        print(tasks[i1-1])
        i2 =int (input("Enter Task B: "))
        print(tasks[i2-1])
        tasks[i1-1],tasks[i2-1] = tasks[i2-1],tasks[i1-1]      
# Exit ########################################## 
    if option == 0:            
        break
    
    



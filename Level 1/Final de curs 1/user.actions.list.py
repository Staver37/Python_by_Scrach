# using  thelist as STACK
#app -> remember USER ACTION HISTORY
#LIFO

from ast import Break

from matplotlib.pyplot import step


ua = []
while True:
    action =input ("Enter an action name: ")
    if action =="":
        break
    ua.append(action)

steps = len(ua)

print("You've made:", steps,"steps")

retrace_steps = int(input("How many to go back? "))
# not longher than number of steps
while len(ua) > 0 and retrace_steps !=0:
    action = ua.pop(len(ua)-1)# cut elemen
    print("deleting step >> ", action)
    retrace_steps -= 1
print(ua)    
    
    
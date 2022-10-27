from os import system
system("clear")

# create function that corespond to: * / + -
# pure function
def mul(a, b):
    return a * b

def div(a,b):
    return a/b

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

# HW1: add(), sub()
# HW2: rewrite: r = 1 + 2 * 3 / 4 

a = add(1,2)
b = mul(a,3)
r= div(b,4)

c = sub(10,1)

print(r)
print(c)

print("\n"*5)
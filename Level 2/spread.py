 # spread , unpack, ... operator

 # CONTEXT: list , dict + functions

l = [1,2,3]
d = {'a':1, 'b':2, 'c':3}

#a,b,c, = d  #<----- unpack
#print(a,b,c)



def f(a,b,c):
    print(a,b,c)
f(**d)
f(*d)    
print(l)
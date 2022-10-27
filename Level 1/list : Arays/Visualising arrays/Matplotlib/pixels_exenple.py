data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
    [0, 0, 0, 1, 2, 2, 1, 0, 0, 0], 
    [0, 0, 0, 1, 2, 3, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    ]

from random import randint
from matplotlib import pyplot



# blur
#for ri in range (9):
#    for ci in range (9):
#        print (data[ri][ci])

#        pixel = (data [ri][ci] + data [ri][ci+1]+data [ri+1][ci]+ data [ri+1][ci+1])
#        data [ri][ci] = pixel

# add noise
#for ri in range (9):
#    for ci in range(9):
#        if randint(1,2) ==1:
#            data[ri][ci] = 0.3

# Scale
data_small = [data
    [0, 0, 0, 0, 0],              
    [0, 0, 0, 0, 0],              
    [0, 0, 0, 0, 0],              
    [0, 0, 0, 0, 0],              
    [0, 0, 0, 0, 0],              
]
for ri in range (5):
    for ci in range (5):
        print (data[ri][ci])

        pixel = (data [ri][ci] + data [ri][ci+1]+data [ri+1][ci]+ data [ri+1][ci+1])
        data [ri][ci] = pixel


pyplot.imshow(data,cmap = 'gray')
pyplot.show()


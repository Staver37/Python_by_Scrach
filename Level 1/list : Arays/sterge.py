array_input = [ [10,12,14] ,[0 ,1 ,2 ] ]
print(array_input[0]) # printing elements of row 0
print(array_input[1]) # printing elements of row 1

size = int(input()) 
array_input = [00]
for x in range(size):
    array_input.append([int(y) for y in input().split()])
print(array_input)
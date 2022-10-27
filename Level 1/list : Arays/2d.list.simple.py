from os import system
system("clear")

# 2 level lists  / bidimansional list
matrix= [
    [1,2,3], # 0
    [4,5,6], # 1
    [7,8,9], # 2
   # 0,1,2
]
# HW1 add the posibility to insert a value from kb

ri = int(input("Row>>>"))
ci = int(input("Colom>>>"))
val = int(input("Val>>"))
matrix[ri][ci]=val

# print the matrix interative

for ri in range (3):
      for ci in range(3):
          print(matrix[ri][ci],end=" ")
      print()

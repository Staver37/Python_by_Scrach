# swap 2 index in a LIST
values = [10,20,30,40,50,60,70]
#             ^       ^
# index       1       4
#            ia       ib
ia = int(input("FIRST:    ")) -1
ib = int(input("SECOUND:  ")) -1

print("Before: ", values)
values[ib],values[ia] = values[ia],values[ib]
print("After: ", values)
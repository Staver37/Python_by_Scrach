
from os import system

system("clear")

## data procesing / 2d lists

## Simulate Temperature Value for April (1 month)

#  * lists
#  * biodimensional lists
#  * loops
#  * conditionals
#  * sun , avg , min, max, flat
#  * ploting

week = 0
day  = 0
wn   = 0


mounth_name = "Aprill"
days_name =["Mo","Tu","Wd","Th","Fr","Sa","Su"]
mounth_temps = [
    # days ------->  
    # Mo   Tu   Wd   Th   Fr   Sa   Su
    [None,None,None,None, 5.0, 6.0, 7.0,],  # |
    [ 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0,],  # |
    [ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0,],  # V
    [ 8.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0,],  # < weeks
    [ 3.0, 2.0, 1.0, 2.0, 3.0, 4.0, None,],

]
# flattan the bidimentional lists
mounth_temps_1d = []
for wi in range(5):
    for di in range (7):
       if mounth_temps[wi][di]!= None:
            mounth_temps_1d.append(  mounth_temps[wi][di]  )

#print(mounth_temps_1d)

max_temp = max(mounth_temps_1d)
min_temp = min(mounth_temps_1d)
sum      = sum(mounth_temps_1d)


# HW 2.4 :calculate the average temp

# INPUT WEEK 
# week =int (input("week>>>"))
#week = week - 1


###########Display The Calendar#################
# Header
print("-------------------------------------------------------------")
print(f"| {mounth_name:54}|   |")
print("-------------------------------------------------------------")
# Days name
for di in range(7):
    print(f"|  {days_name[di]}   ",end="")
print("|   |") 
print("-------------------------------------------------------------")
date = 1
# Loop through the weeks
for wi in range (5):
    wn += 1
    #   Temps for ONE WEEK
    for di in range(7):
        if mounth_temps[wi][di] == None:
           date_str=" " * 6 
        else:
            date_str = date
            date += 1
        print(f"| {date_str:<6}",end="")    
    print("|   |")    
    
    # HW 2.2 add the ROW with the week nr here
    ###############################################
    for di in range(7):
        print(f"|       ",end="")
                
    print(f"| {wn} |") 
    ###############################################
    for di in range(7):
        # HW 2.1 rewrite this code using standard if/else
        temp = f"{mounth_temps[wi][di]:5.1f} " if mounth_temps[wi][di] != None else" "* 6
        print(f"|{temp} ", end="")
    
    print("|   |")   
    print("-------------------------------------------------------------")
###########Display The Calendar#################

print(f"Max_temp: {max_temp}")
print(f"Min temp:{min_temp}")
print(f"Sum:{sum}")
print("Average:",sum % di)



#print(f"today's temperature {mounth_temps[week][day]:7.2}C") 
# print("forecast for entire week:")

# for day_index in range (7) :
#    print(f"t:{mounth_temps[week][day_index]:7.2}C")




#  -------------------------------------------------------------
#  |  Mo   |  Tu   |  Wd   |  Th   |  Fr   |  Sa   |  Su   |  |
#  -------------------------------------------------------------
#  |       |       |       |       | 1     | 2     | 3     |  |
#  |       |       |       |       |       |       |       |1 |
#  |       |       |       |       |  5.0  |  6.0  |  7.0  |  |
#  -------------------------------------------------------------
#  | 4     | 5     | 6     | 7     | 8     | 9     | 10    |  |
#  |       |       |       |       |       |       |       |2 |
#  |  8.0  |  7.0  |  6.0  |  5.0  |  4.0  |  3.0  |  2.0  |  |
#  -------------------------------------------------------------
#  | 11    | 12    | 13    | 14    | 15    | 16    | 17    |  |
#  |       |       |       |       |       |       |       |3 |
#  |  1.0  |  2.0  |  3.0  |  4.0  |  5.0  |  6.0  |  7.0  |  |
#  -------------------------------------------------------------
#  | 18    | 19    | 20    | 21    | 22    | 23    | 24    |  |
#  |       |       |       |       |       |       |       |4 |
#  |  8.0  |  9.0  |  8.0  |  7.0  |  6.0  |  5.0  |  4.0  |  |
#  -------------------------------------------------------------
#  | 25    | 26    | 27    | 28    | 29    | 30    |       |  |
#  |       |       |       |       |       |       |       |5 |
#  |  3.0  |  2.0  |  1.0  |  2.0  |  3.0  |  4.0  |       |  |
#  -------------------------------------------------------------

#    #HW 2.3 try to create helper function to simplifi the code

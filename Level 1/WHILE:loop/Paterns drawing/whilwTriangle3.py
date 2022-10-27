from os import system
system("clear")

#            *
#          * *
#        * * *
#      * * * *
#    * * * * *




##########################
index = 6
loop_index = 0
while loop_index < index:
    
    sub_loop_index1 = 0
    while sub_loop_index1 <=  loop_index:
        print("2",end="")
        sub_loop_index1 += 1
         
    sub_loop_index2 = index - loop_index
    while sub_loop_index2 > 1:
        print("*", end="")
        sub_loop_index2 -= 1
          
   
    sub_loop_index3 = index - loop_index
    while sub_loop_index3 > 1:
        print("*", end="")
        sub_loop_index3 -=1
    
    sub_loop_index4 = 0
    while sub_loop_index4 <=  loop_index:
        print("1",end="")
        sub_loop_index4 += 1 
   
    print("")
    loop_index += 1  
    
##########################

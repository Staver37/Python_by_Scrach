# x------------R------------>
# 0

batteryCharge = 70  #  5%
ratePerSteps  = 10   # 10%/m

steps = 0

# COMPLEXITY
# DRY -Don't Repeat Yourself

while batteryCharge > 0:
# #########one step##########################################
    steps         += 1      #increment
    batteryCharge -= ratePerSteps
    print("steps: " , steps,"baterry: ", batteryCharge , "%")
    if batteryCharge<=10:
        print("WARNING!!! Need to charge")
# ##########one step##########################################

## INS:
## start time: HH:MM
## end   time: HH:MM

## OUT:
##  duration in minutes
# 24H format 
# test1: "10:05" ---> "10:15" = 10
# test2: "10:05" ---> "11:15" = 70 Gresit
# test3: "11:15" ---> "12:05" = 50
# test4:"22:45"  ---> "01:30" =165

# integer numbers
start_time = input("start time(HH:MM):  ")
start_time_h = int( start_time[0:2] )
start_time_m = int( start_time[3:5] )

end_time = input("end time (HH:MM):  ")
end_time_h = int(end_time[0:2] )
end_time_m = int(end_time[3:5] )

duration_h = end_time_h - start_time_h
duration_m = end_time_m - start_time_m

duratio_m_f = duration_h * 60 + duration_m + 24 * 60 * (start_time_h > end_time_h)

# HW1: calculate and print duration: HOURS + MINUTES (2H 45M)

print("event duration:", duratio_m_f  , "minutes")

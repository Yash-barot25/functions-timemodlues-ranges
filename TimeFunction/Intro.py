import time

print(time.gmtime(0))

print(time.localtime())

print(time.time())

current_time = time.localtime()

print(current_time)

print("Year: ", current_time[0], current_time.tm_year)
print("Month: ", current_time[1], current_time.tm_mon)
print("Day: ", current_time[2], current_time.tm_mday)
print("Time: ", current_time.tm_hour, ":", current_time.tm_min, ":", current_time.tm_sec)

import time
from time import process_time as my_timer
# from time import perf_counter as my_timer
# from time import time as my_timer
# from time import monotonic as my_timer
import random

# print(my_timer())
input("Press enter to start")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")
end_time = my_timer()

print("start time: " + time.strftime("%X", time.localtime(start_time)))
print("end time: " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} sec.".format(end_time - start_time))



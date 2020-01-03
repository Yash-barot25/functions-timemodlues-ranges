import time

current_time = time.localtime()

while True:
    print("Time: ", current_time.tm_hour, ":", current_time.tm_min, ":", current_time.tm_sec)
    time.sleep(1)

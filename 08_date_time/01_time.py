import time
print(time.localtime(time.time()))
# time.struct_time(tm_year=2025, tm_mon=1, tm_mday=21, tm_hour=11, tm_min=54, tm_sec=31, tm_wday=1, tm_yday=21, tm_isdst=0)

print(time.asctime(time.localtime(time.time())))
# Tue Jan 21 11:55:35 2025
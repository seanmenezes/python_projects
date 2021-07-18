from  datetime import datetime
import time
dt = datetime(2018,1,1)
print(dt)
current_dt = datetime.now()
print(current_dt)
strp_time = datetime.strptime("2018/01/01","%Y/%m/%d")
print(strp_time)

from_timestamp = datetime.fromtimestamp(time.time())
print(from_timestamp)

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))

print( dt < current_dt)


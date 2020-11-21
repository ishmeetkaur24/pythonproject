#WAp to Display current date and time

import datetime
import time

currentDate = datetime.datetime.today()
print (currentDate)

for i in range(100):
    TodayTime = datetime.datetime.today()
    print(TodayTime)
    time.sleep(2)
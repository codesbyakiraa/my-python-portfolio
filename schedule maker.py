import schedule
import time as tm
from datetime import time,timedelta,datetime

def task():
    print("take a break, life is short!")
schedule.every(5).seconds.do(task)
while True:
    schedule.run_pending()
    tm.sleep(1)

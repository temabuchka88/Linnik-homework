from datetime import datetime
import time
def timedata (n):
    dt = []
    for x in range(n):
        dt.append(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
        time.sleep(1)
    return dt
repeat = int(input('Введите количество повторений: \n'))
print(timedata(repeat))
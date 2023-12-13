from datetime import datetime

def working_hours_only(func):
    def wrapper():
        time_now = datetime.now()
        hours = time_now.hour
        if hours in range(9,19):
            func()
        else:
            print('Работать нельзя!')
    return wrapper

@working_hours_only
def work():
    print('Работаем')

work()


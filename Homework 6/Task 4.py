from datetime import datetime

def my_decorator(func):
    def wrapper():
        start_time = datetime.now()
        func()
        func_time = datetime.now() - start_time
        print(f'Время выполнения: {func_time} ')
    return wrapper

@my_decorator
def my_func_1():
    arg_1 = int(input('Введите первое число\n'))
    arg_2 = int(input('Введите второе число\n'))
    arg_3 = arg_1 - arg_2
    print(arg_3)

my_func_1()

@my_decorator
def my_func_2():
    even_or_odd = lambda num: 'Это число нечетное' if num % 2 else 'Это число четное'
    number = int(input('Введите число\n'))
    print(even_or_odd(number))

my_func_2()
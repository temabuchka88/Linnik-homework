def string_analysis(func):
    def wrapper(value):
        try:
            string_to_float = float(value)
        except ValueError:
            print(f'Вы ввели не корректное число: {value}')
            return

        if '.' in value:
            integer_or_fraction = 'дробное'
            string_to_int = float(value)
        else:
            integer_or_fraction = 'целое'
            string_to_int = int(value)

        if string_to_int > 0:
            positive_or_negative = 'положительное'
        else:
            positive_or_negative = 'отрицательное'
        print(f'Вы ввели {positive_or_negative} {integer_or_fraction} число: {value}')
        func(value)
    return wrapper

@string_analysis
def mystring(value):
    pass

mystring(input('Введите значение:\n'))
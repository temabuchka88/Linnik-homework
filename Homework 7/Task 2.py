def my_decorator(correct_type):
    def funcc(func):
        def wrapper(value):
            type_value = type(value)
            if type_value == correct_type:
                print(f'Тип аргумента - {correct_type.__name__}')
                return func(value)
            else:
                print('Введен неверный аргумент')
        return wrapper
    return funcc

@my_decorator(int)
def times2(value):
    return value*2
print(times2(4))
print(times2(True))

@my_decorator(str)
def first_letter(word):
    return word[0]
print(first_letter('Hello'))
print(first_letter(True))

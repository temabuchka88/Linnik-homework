def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
number = int(input('Введите число, для определения факториала\n'))
print(factorial(number))

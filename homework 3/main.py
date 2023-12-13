 # Task 1
phrase = (input('Введите фразу из двух слов: \n'))
print(f'!{phrase.split()[1]} ! {phrase.split()[0]}!')
last_phrase = phrase.split()
print('!{} ! {}!'.format(last_phrase[1], last_phrase[0]))
print('!%s ! %s!'%(last_phrase[1], last_phrase[0]))
 # Task 2
name = input('Введите ваше имя: \n')
age = input('Введите ваш возраст: \n')
if not age.isdigit():
    print('Ошибка, повторите ввод')
elif int(age) <= 0:
    print('Ошибка, повторите ввод')
elif int(age) > 0 and int(age) < 10 and int(age) != 10:
    print(f'Привет, шкет {name}')
elif int(age) >= 10 and int(age) <= 18:
    print(f'Как жизнь {name}?')
elif int(age) > 18 and int(age) < 100:
    print(f'Что желаете {name}?')
else:
    print(f'{name}, вы лжете - в наше время столько не живут...')
 # Task 3
while True:
    second_name = input('Введите ваше имя: \n Если хотите остановить программу введите "stop"\n')
    if second_name == 'stop':
        break
    second_age = input('Введите ваш возраст: \n. Если хотите остановить программу введите "stop"\n')
    if second_age == 'stop':
        break
    if not second_age.isdigit():
        print('Ошибка, повторите ввод')
    elif int(second_age) <= 0:
        print('Ошибка, повторите ввод')
    elif int(second_age) > 0 and int(second_age) < 10 and int(age) != 10:
        print(f'Привет, шкет {second_name}')
    elif int(second_age) >= 10 and int(second_age) <= 18:
        print(f'Как жизнь {second_name}?')
    elif int(second_age) > 18 and int(second_age) < 100:
        print(f'Что желаете {second_name}?')
    else:
        print(f'{second_name}, вы лжете - в наше время столько не живут...')
 # Task 4.1
n = int(input('Введите целое число:\n'))
sum_qube = []
x = 0
for a in range (1, n+1):
    a **= 3
    sum_qube.append(a)
for b in sum_qube:
    x += b
print(x)
 # Task 4.2
n = int(input('Введите целое число:\n'))
sum = 0
a = 1
while a <= n:
    sum += n**3
    n -= 1
print(sum)
 # Task 5
from random import randint
while True:
    x = randint(1, 10)
    break
answer = int(input('Вам нужно угадать число от 1 до 10, введите свой вариант:\n'))
true_answer = answer
while answer == x:
    print('Поздравляю, вы угадали')
    break
else:
    while answer !=x:
        exta_try = int(input('Увы, вы не угадали, введите число еще раз:\n'))
        if exta_try == x:
            print('Поздравляю, вы угадали')
            break
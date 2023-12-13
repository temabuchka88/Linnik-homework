from random import randint
from operator import itemgetter
all_random_numbers = []
number_of_repetitions = []
while len(all_random_numbers) != 15:
    random_number = randint(0, 9)
    all_random_numbers.append(random_number)
for value in all_random_numbers:
    number_of_repetitions.append(all_random_numbers.count(value))
# print(all_random_numbers) ##### Вывод чисел
# print(number_of_repetitions) ##### Вывод количества повторений
all_numbers_dict = dict((zip(all_random_numbers, number_of_repetitions)))
print(all_numbers_dict) ###### Словарь со всеми числами
sorted_numbers_dict = dict(sorted(all_numbers_dict.items(), key=itemgetter(1), reverse=True))
repeat_numbers = dict(list(sorted_numbers_dict.items())[:3])
print(repeat_numbers)
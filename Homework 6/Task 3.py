my_words = ('радар', 'анна', 'ротор', 'дом', 'level', 'шалаш', 'довод', 'телефон', 'Артём')
palindromic_words = filter(lambda word: word == word[::-1], my_words)
result = tuple(palindromic_words)
print(result)
 #1
a = b = c = 5
print(id(a), id(b), id(c), sep = ', ')
print(a, b, c, sep = ', ')
 # 2
d = 3
e = '3'
print(id(d), id(e), sep = ', ')
print(d, e, sep = ', ')
 #3
a_1 = str(5)
b_1 = int(5)
c_1 = float(5)
d_1 = 3
e_1 = 3
print(id(a_1), id(b_1), id(c_1), id(d_1), id(e_1), sep = ', ')
 #4
phrase = str(input('Введите строку \n'))
even_letters = phrase[1:len(phrase):2]
odd_letters = phrase[0:len(phrase):2]
print('Введенная строка:',phrase, end='\n'*3)
print(even_letters, odd_letters, sep=' '*5, end='\n!!!')
my_code = b'r\xc3\xa9sum\xc3\xa9'
my_decode = my_code.decode('UTF-8')
my_encode_latin = my_decode.encode("Latin 1")
my_decode_latin = my_encode_latin.decode("Latin 1")
print(my_decode)
print(my_encode_latin)
print(my_decode_latin)
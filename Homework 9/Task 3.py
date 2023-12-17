import json

my_dict = {123456 : ('Mark', 22), 123457 : ('Jack', 40), 123458 : ('Arden', 25), 123459 : ('Birdie', 30),
        1234510 : ('Oscar', 33), 123460 : ('Lucy', 51), 123461 : ('James', 21),}

with open('Homework 9\\task_3_file.json', 'w') as file:
    json.dump(my_dict, file)
    file.close()
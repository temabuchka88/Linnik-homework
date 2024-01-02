def fib(n):
    num_1, num_2 = 0, 1
    for a in range(n):
        num_1, num_2 = num_2, num_1 + num_2
        yield num_1


asd = 10
print(list(fib(7)))

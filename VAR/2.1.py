# 2.1. Разработать функцию, возвращающую список чисел ряда Фибоначчи с использованием бесконечных итераторов (модуль itertools).

from itertools import islice

class generator:
    def __init__(self):
        self.fib1 = 0
        self.fib2 = 1
    def __next__(self):
        result = self.fib1
        self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2
        return result
    def __iter__(self):
        return self

f = generator() 

st = int(input("От какого числа: \t" ))
end = int(input("До какого числа: \t" ))

print(list(islice(f, st, end))) 

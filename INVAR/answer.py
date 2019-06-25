# Задание 2.1

n = int(input('Введите максимальное число: '))

if n < 2:
    quit()

print(number1, end=' ')
print(number2, end=' ')

def func(value):
    number1 = 0
    number2 = 1
    while number2<value:
        number1, number2 = number2, number1 + number2
        print(number2, end=' ')
    
res = []
res = func(n)
    
# Задание 2.2

n = int(input('Введите максимальное число: '))

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


print('Ответ: ')
for i in generator():
    print(i, end=' ')

    if i >= n:
        break
        
 
 # Задание 2.2
 
 value = int(input("Введите максимальное число: \t" ))

def fib(value):
  lst = [0, 1, ]
  it = iter(list(range(2, value)))
  while True:
    try:
      elem = next(it)
    except StopIteration:
      break
    n = lst[elem - 1] + lst[elem - 2]
    lst.append(n)
  return lst

res = fib(value)
print(res)

if __name__ == "__main__":
    assert(fib(3) == [0,1,1,2,3])
    assert(fib(5) == [0,1,1,2,3,5])
    assert(fib(8) == [0,1,1,2,3,5,8])

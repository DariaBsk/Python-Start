

import random

number = int(input())
maxRandom = int(input('input max random number'))
maxAmount = 0

list = []
count = [0] * (maxRandom+1)

for i in range(0, number):
    list.append(random.randint(0, maxRandom))

for i in list:
    count[int(i)] += 1

for i in count:
    if i > maxAmount:
        i = maxAmount

print(list)
print(count)
print('МАскимально количество раз появилась ' + str(count[maxAmount]) + ', ' + str(maxAmount+1) + ' раз')


# Евгений
import random

number = int(input())
maxRandom = int(input('input max random number'))
maxAmount = 0

От Sergey R всем 10:10 PM
import random

a = 1
b = 6

array = [random.randint(a, b) for i in range(20)]
print(array)

d = {}

for i in array:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
    
print(d)

max = 0
for i in range(a, (b+1)):
    if(d[i] > max):
        max = d[i]

print(f"Максимальное повторение элемента {max} раз.")

# import random
import random

a = 1
b = 6

array = [random.randint(a, b) for i in range(20)]
print(array)

print(set(array))
d = {}

for i in array:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

max = 0
for i in range(a, (b + 1)):
    if (d[i] > max):
        max = d[i]

print(f"Максимальное повторение элемента {max} раз.")

import random

number = int(input())
maxRandom = int(input('input max random number'))
maxAmount = 0

list = []
count = [0] * (maxRandom+1)

for i in range(0, number):
    list.append(random.randint(0, maxRandom))

for i in list:
    count[int(i)] += 1

for i in count:
    if i > maxAmount:
        i = maxAmount

print(list)
print(max(count))
print('МАскимально количество раз появилась ' + str(count[maxAmount]) + ', ' + str(maxAmount+1) + ' раз')


адайте список из n чисел 
От Артур всем 10:30 PM
3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
    
    *Пример:*
    
    - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
    Сумма 9.06
адайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

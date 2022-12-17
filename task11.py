11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
    *Пример:*
    
    - Для N = 5: 1, -3, 9, -27, 81
number = int(input('Input N '))

list = []

for i in range(0, number):
    list.append((-3) ** i)

print(list)

12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
    *Пример:*
    N = int(input('input n '))

dict = {}

for i in range(1, N+1):
    dict.setdefault(i, (3*i+1))

print(dict)

    - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
#  Напишите программу, в которой пользователь будет задавать две строки,
#  а программа - определять количество вхождений одной строки в другой.
one = input('Input string ')
two = input('Input secons string ')

counter = 0

list = []

if len(two) == 1:
    for i in one:
        list.append(i)
else:
    list = one.split(' ')

print(list)

for i in list:
    if two in i:
        counter += 1

print(counter)


# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# n = int(input())
# a = {}
# for i in range(1,n+1):
#     a[i] = i*3+1
# print(a)


print (one_str.count (two_str))
one_str[i:i+len(two_str)] == two_str

one = input('Input string ')
two = input('Input secons string ')
count = 0
for i in range(len(one) - len(two) + 1):
    if one[i:i+len(two)] == two:
#От Артур всем 09:29 PM
one = input()
two = input()
# count = 0
# for i in range(len(one)-len(two)+1):
#     if one[i:i+len(two)] == two:
#         count += 1
# print(count)
print(one.count(two))

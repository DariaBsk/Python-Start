# ФАЙЛЫ
# a - открытие для добавления данных; если файла нет, то он будет создан
# r - открытие для чтения данных
# w - открытие для записи данных - перезапись с удалением предыдущего
# w+ r+


# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()

with open('file.txt', 'w') as data: # не нужно закрывать в ручном режиме
    data.write('line1\n') 
    data.write('line2\n')



exit() # функция, которая позволяет не выполнять далее записанный код
path = 'file.txt'# xntybt
data = open(path, r)
for line in data:
    print(line)
data.close()


# Функции и Модули

import lec # вызов функции из другого файла

print(lec.f(1))

# или

import lec as l #для упрощения упоминания файла

print(l.f(1))


def new_string(symbol, count):
    return symbol * count

print(new_string('!', 5)) # !!!!!
print(new_string('!')) # Type Error, НО count можно задать заранее

def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5)) # !!!!!
print(new_string('!')) # !!!
print(new_string('4')) # 12

def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w')) # asdw, склеивание строк
print(concatenatio('a', '1')) # a1
# print(concatenatio(1, 2, 3, 4)) # TypeError

# РЕКУРСИЯ - функция, вызывающая сама себя

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1)+ fib(n-2)

list = 1
for e in range(1, 10):
    list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34

# КОРТЕЖ - это неизменяемый список

a = (3, 1, 41, 4)
print(a)
print(a[-1])
a[0] = 12 # не работает
# кортеж из 1 элемента
a = (3,) # поставим запятую

a = (3, 4, 5)
for item in a:
    print(item)

t = tuple(['red', 'green', 'blue']) #создаем список и конвертируем его в кортеж
red, green, blue = t #распаковываем кортеж и превращаем его в три независимых переменных
print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red, g:green, b:blue

# СЛОВАРИ - неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {} # пустой словарь
dictionary = \
    {
        'up': '^' # Слева ключ латиницей, справа значение - стрелочка
        'left': '<'
        'down': 'v'
        'right': '>'
    }
print(dictionary) # { 'up': '^', 'left': '<', 'down': 'v', 'right': '>' }
print(dictionary{'left'}) #
# Типы ключей могут отличаться

for k in dictionary.keys():
    print(k) # ключи
    
for k in dictionary.values():
    print(k) # значения

dictionary['up'] = 'up' # меняется значение

# МНОЖЕСТВА

colors = {'red', 'green', 'blue'}
# print(type(colors)) # тип данных set
print(colors) # {'red', 'green', 'blue'}
colors.add('red') # добавить элемент
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue', 'gray'}
colors.remove('red') # удалить элемент
print(colors) # {'green', 'blue', 'gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue', 'gray'}
colors.clear() # {}
print(colors) # set()


a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} Объединение множеств
i = a.intersection(b) # i = {8, 2, 5} 
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}

q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}

s = frozenset() # Неизменяемое множество

# СПИСКИ

list1 = [1,2,3,4,5]
list2 = list1

list1[0] = 123 # замена в обоих списках
list2[1] = 333 # замена в обоих списках

print() # печать пустой строки

for e in list1:
    print(e)

print() # печать пустой строки

for e in list2:
    print(e)

# Как удалять последний элемент

list1 = [1,2,3,4,5]

print(list1.pop()) # удаление последнего элемента
print(len(list1)) # сколько элементов в нашем листе
print(list1) # печатаем список после удаления элемента
print(list1.pop()) 
print(list1) 
print(list1.pop()) # удаление каждого последнего элемента
print(list1)
print(list1.pop()) 
print(list1) 

print(list1.pop(2)) # удаление определенного элемента

print(list1.insert(2, 11)) # добавление элемента, где 2 - позиция, 11 - значение

print(list1.append(11)) # добавление в конец элемента 11
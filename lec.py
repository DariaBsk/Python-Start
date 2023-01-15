#print("Hello world")

#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
    
 #   *Примеры:* 
    
  #  - 5, 25 -> да
   # - 4, 16 -> да
    #- 25, 5 -> да
    #- 8,9 -> нет
#print ("Введите первое число: ")   

#print ("Введите второе число: ")  

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))

# if a == b*b or b == a*a:
#     print ("Число является квадратом другого числа")
# else:
#     print ("Число не является квадратом другого числа")

# print("Введите число: ")

# f = int(input())
# a ="   _~_    \n"
# b ="  (0 0)   \n"
# c =" /  v  \  \n"
# d ="/(  _  )\ \n"
# e ="  ^^ ^^   \n"

# print(f*str(a+b+c+d+e))

# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))
# # value = 12334
# # print(value)
# s = 'hello world'
# # print(s) #вывод строки
# # \n - c новой строки

# print(a,'-', b,'-', s)
# print('{} - {} - {}'. format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}'. format(a, b, s))

# f = True
# print(f)

# list = ['1', '2', '3' ]
# print(list)
# #ввод и вывод данных
# #print, input

# print('Введите a')
# a = input()
# # a = int(input())
# # a = float(input())
# print('Введите b')
# b = input()
# # b = int(input())
# # b = float(input())
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# # / деление вещественных чисел
# # // деление нацело
# # % остаточное деление
# # ** возведение в степень

# a = 1.3
# b = 3
# c = round(a * b, 5)
# print(c)
# # a = a + 5 или a += 5

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen


# # Логические выражения
# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_odd = f[0]%2 == 0
# print(is_odd)


# a = int(input('a = '))
# b = int(input('b = '))
# if a>b:
#     print(a)
# elif a == b:
#     print(f'{a} = {b}')
# else:
#     print(b)


# original = 123 # переворачивание числа
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй, хватит')
# print(inverted)

# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# list = [1, 2, 3, 4, 10, 5]
# for i in list:
#     print(i**2)

# r = range(10) #cписок из 10 первых элементов, то есть, от 0 до 9
# for i in r:
#     print(i)

# for i in range(5): #cписок из 5 первых элементов, то есть, от 0 до 4
#     print(i)

# for i in range(1, 10, 2): #cписок из элементов, где 1 это начальный элемент, 10 - конечный, 2 - шаг.
#     print(i) # список из нечетных элементов

for i in 'qwe - rty':
    print(i)# разбивает строку на символы

# НЕМНОГО О СТРОКАХ

text = 'съешь ещё этих мягких французских булок'
print(text)
print(len(text))                    #39
print('ещё' in text)                #True
print(text.isdigit())               #False - являются ли все элементы числами
print(text.islower())               #True - все элементы в нижнем регистре
print(text.replace('ещё', 'ЕЩЁ'))   #хотим что-то заменить

for c in text:
    print(c)

# text. нажимаем Ctrl пробел - подсказки функций: help(text.istitle) - справка от Python - help(int), help(str)

# СРЕЗЫ
for c in text:
    print(c)

text = 'съешь ещё этих мягких французских булок'
print(text[0])                          # с
print(text[1])                          # ъ
print(text[len(text)])                  # IndexError
print(text[len(text)-1])                # к
print(text[-5])                         # 6
print(text[:])                          # print(text) => [0:len(text)-1]
print(text[:2])                         # cъ => [:2], [0:2]
print(text[len(text)-2:])               # ок
print(text[2:9])                        # ешь еще
print(text[6:-18])                      # еще этих мягких
print(text[0:len(text):6])              # сеикакл
print(text[::6])                        # сеикакл
text = text[2:9] + text[-5] + text[:2]  # 


# СПИСКИ - пронумерованная изменяемая коллекция элементов типов

numbers = [1, 2, 3 ,4, 5]
print(numbers) # [1, 2, 3 ,4, 5]

numbers = list(range(1, 6))
print(numbers) # [1, 2, 3 ,4, 5]

numbers[0] = 10
print(numbers) # [10, 2, 3 ,4, 5]

for i in numbers:
    i *= 2
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [1, 2, 3 ,4, 5]

# СПИСКИ: введение
## list = list

numbers = [1, 2, 3 ,4, 5]
print(numbers) # [1, 2, 3 ,4, 5]
ran = range(1, 6)
print(type(ran))
numbers = list(ran) # приведение типа ran к типу list
print(type(numbers))

print(numbers)
numbers[0] = 10
print(f'{len(numbers)} len')

colors = ['red', 'green', 'blue']

for e in colors:
    print(e*2) # redred greengreen blueblue

colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') # del colors[0] # удалить элемент
del colors[0] # удалить элемент


# ФУНКЦИИ - это фрагмент программы, используемый многократно

# def function_name(x):
    # body line 1
    # ...
    # body line n
    # optional return

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))
print(type(f(arg)))


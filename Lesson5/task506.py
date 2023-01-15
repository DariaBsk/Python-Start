#Вычислить число c заданной точностью d
#при $d = 0.001, π = 3.141.$
# import math
# n = input()
# length = len(n.split(".")[1])
# print(round(math.pi,length))

#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# n = int(input())
# list_num = []
# cur_num = 2
# while n!=1:
#     if n%cur_num==0:
#         list_num.append(cur_num)
#         n = n//cur_num
#         cur_num = 2
#     cur_num +=1
# print(list_num)

#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# n = int(input())
# list_num = []
# cur_num = 2
# while n!=1:
#     if n%cur_num==0:
#Задайте последовательность чисел.
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
a = [1,1,2,3,4,5,5,6]
list_num = []
#print(set(a))
for i in a:
    if a.count(i) == 1:
        list_num.append(i)
print(list_num)


#Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
import random
k = int(input())
result = ""
for i in range(k,-1,-1):
    koeff = random.randint(0,3)
    if koeff == 0:
        continue
    if koeff == 1:
        if i == 1:
            result += f"x+"
        elif i == 0:
            result += f"{koeff}"
        else:
            result += f"x**{i}+"
    else:
        if i == 1:
            result += f"{koeff}*x+"
        elif i == 0:
            result += f"{koeff}"
        else:
            result += f"{koeff}*x**{i}+"
result += " = 0"
print(result)

f = open("filepol.txt","w")
f.write(result)
f.close()



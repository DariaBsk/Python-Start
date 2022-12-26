# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def ProductList(list_n):
    firstPart = []
    lastPart = []
    list_prod = []
    for x in range(0, (len(list_n)//2)):
        firstPart.append(list_n[x])
    for i in range(len(list_n)-1, ((len(list_n)//2)-1), -1):
        lastPart.append(list_n[i])
    j = 0
    while j < (len(list_n)//2):
        list_prod.append(firstPart[j]*lastPart[j])
        j = j+1
    return list_prod

def ProductList_nItself(list_n):
    if len(list_n) % 2 == 0:
        list_prod = ProductList(list_n) 
    else: 
        t = list_n[(len(list_n)//2)]  
        list_n.remove(t)
        list_prod = ProductList(list_n)     
        list_prod.append(t*t)
    return list_prod

n=int(input('Введите размер списка: '))

list_rd = list(random.sample(range(1, 20), n))

print(f"{list_rd} => {ProductList_nItself(list_rd)}")
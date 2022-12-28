# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

def SearchRepeatNumbers(list_string):
    new_lst = []
    i = 0
    while i < len(list_string):
        l = list_string[i]
        if (list_string.count(l)) == 1:
            new_lst.append(l)
        i = i+1
    list_int = list(map(int, new_lst))
    return list_int

list_s = list(input("Введите числа:").split())
list_i = list(map(int, list_s))

print(f'{list_i} => {SearchRepeatNumbers(list_s)}')

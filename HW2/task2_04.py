# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

print('Введите натуральное число: ')
N = int(input())
list_num = list(range(-N, N+1))
print(list_num)
new_el = 1
text = open('file2_04.txt')
print()
for line in text:
       new_el *= list_num[int(line)]
text.close
print('Произведение элементов:  ', new_el)


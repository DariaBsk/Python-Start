# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print("Введите номер дня недели: ") 
f = int(input())
if 1 <= f <= 5:
    print("Это рабочий день")
elif 6 <= f <= 7:
    print("Это выходной день")
else:
    print("Некорректные данные")
    
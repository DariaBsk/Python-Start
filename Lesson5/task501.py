# 35. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

print('Введите последовательность натуральных чисел через пробел')
data = list(map(int,input().split()))
for i in range(len(data)-1,-1,-1):
    if i > 0:
        number = data[i]
        n = data[i-1]
        if number - 1 != n:
            x = number-1
            data.append(x)

print(f'Нужное нам чило = {x}')

# 2 sposob

list1 = [1, 3, 4, 5, 6, 7]

def find(list):
    for i in list:
        if list[i] -1 != list[i-1]:
            return list[i] -1
print(find(list1))

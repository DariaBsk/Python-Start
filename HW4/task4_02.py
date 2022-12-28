# 2. Задайте натуральное число N.
# Напишите программу, которая составит
# список простых множителей числа N.

def ListPrimeFactorsNumber(num):
    list_mul = []
    i=2
    n=num
    while i*i<=num:
        while num % i==0:
                list_mul.append(i)
                num = num / i
        i = i + 1
    if num > 1:
            list_mul.append(int(num))
    if num == n:
        print (f"У числа {n} нет простых множителей.")
        quit()
    return list_mul

n=int(input('Введите целое положительное число: '))
print (n, ' => ', ListPrimeFactorsNumber(n))
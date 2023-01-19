#lambda, filter, map, zip, enumerate, list comprehension

#list comprehension
#import random

# a = [i for i in range(1,10) if i%2==0]
# print(a)

#enumerate

# a = [2, 4, 6, 8]
# for indx,val in enumerate(a):
#     if val>5:
#         a[indx] = 0
# print(a)

#zip
# a = [1,2,3]
# months = ["june","july","july1","july2","july3","july4"]
# dit_s = {1:"ddd",2:"112"}
# result = list(zip(a,months,dit_s))
# print(result[1][1])

#lambda
# def summ(a,b,*args):
#     for i in args:
#         print(i)
#     return a+b

# 41)Напишите программу на Python для поиска пересечения двух заданных массивов с помощью Lambda, filter.
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]


arr1 = [1, 2, 3, 5, 7, 8, 9, 10]
arr2 = [1, 2, 4, 8, 9]

print(list(filter(lambda x: x in arr1, arr2)))

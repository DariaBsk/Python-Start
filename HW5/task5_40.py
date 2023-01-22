# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.



def encode(s):
 
    encoding = "" 
 
    i = 0
    while i < len(s):
        count = 1

        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1

        encoding += str(count) + s[i]
        i = i + 1
 
    return encoding

a = (input('Введите данные ' ))
print(encode(a))

# def origin_data(m):
#     coding = "" 
#     for i in range(1, len(m)+1, 2):
#         if type(m[i-1]) == int:
#             coding += m[i]*m[i-1]
        
#     return coding

# b = (input('Введите данные ' ))
# print(origin_data(b))
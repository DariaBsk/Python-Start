# 1. Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
d=(input("Введите число π: "))

n=(len(d)-d.find('.'))-1          
p=(round((math.pi*(float(d))),n)) 
print(f'd={d}, π = {p}')
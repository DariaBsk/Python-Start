# Сумма нечетных позиций списка

print("Сумма нечетных позиций списка")
a = [7, 71, 5, 8, 2, 45, 4, 78]
sum = 0
for i in range(1, 8, 2):
    sum += a[i]
print(sum)

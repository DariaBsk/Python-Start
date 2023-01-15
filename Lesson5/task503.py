# 37. Напишите программу, удаляющую из текста все слова, содержащие "абв".
line = 'фывабвйцу кенабвджэ, ячсабвнгш, йцукенгвба'
while ',' in line or '.' in line or ';' in line or ',' in line:
    line = line.replace(',', '')
print(line)

arr = line.split()
print(arr)

for i in range(len(arr)):
    if 'абв' in arr[i]:
          arr.remove(i)
print(arr)





# line = 'фывабвйцу кенабвджэ, ячсабвнгш, йцукенгвба'
# while ',' in line or '.' in line or ';' in line or ',' in line:
#     line = line.replace(',', '')
# print(line)

# arr = line.split()
# print(arr)

# arr2 = []
# for word in arr:
#     if 'абв' not in word:
#         arr2.append(word)
# print(arr2)



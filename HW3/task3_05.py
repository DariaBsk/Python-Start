# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def Febonachi(k):
    a = 0
    b = 1
    count = 0
    f=[]

    if(k <= 0):
       print("Введите целое число: ")
    else:
      while(count <= k) :
           f.append(a)
           c = a + b
           a = b
           b = c
           count += 1
    return (f)

def Negafebonachi(k):   
    a=1
    b=-1
    fn=[]
    k=k*-1
    count = 0

    while (count>k):
       fn.append(a)
       c=a-b
       a=b
       b=c
       count-=1

    return(fn)

def AddingReversalList(list_1,list_2):
    i = 0
    while i<len(list_2):
       list_1.insert(0,list_2[i])
       i+=1
   
    return list_1

k = int(input("Задайте число: "))
febonachi = Febonachi(k)
negafebonachi = Negafebonachi(k)

print(l:=list(((negafebonachi[::-1]) + (febonachi))))

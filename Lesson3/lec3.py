# Анонимные, lambda функции

# def sum(x):
#  return x+10
# def mult(x):
#  return x**2
# sum(mult(2))
# #Анонимные, lambda функции
# def sum1(x):
#  return x+22
# def mult2(x):
#  return x**3
# sum1(mult2(2))
# def sum3(x):
#  return x+242
# def mult4(x):
#  return x**5
# sum3(mult2(2))


# def f(x):
#     return x**3
# print(f(-2))

# sum = lambda a, b: a + b + 1
# def calc(op, a, b):
#     print(op(a, b))
# calc(lambda a, b: a + b +3, 2, 5)

#list = []

# for i in range(1, 101):
#     if i%3 == 0:
#         list.append(i)
# print(list)

# list = [i for i in range(1, 21) if i%2 == 0]
# print(list)

# list = [(i, i*2) for i in range(1, 21) if i%2 == 0]
# print(list)


# def f(x):
#     return x**3
# list = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
# print(list)

data = list(map(int, '1, 2, 3'.split()))
for e in data:
    print(e)
    





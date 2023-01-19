# 43)Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100 (сделать с помощью list_comprehension)
# Имеется список имен сотрудников из 10 элементов (вручную)

# Сопоставьте каждому имени сотрудника его id по порядку, и выведите получившийся список кортежей.
# Отсортировать список по возрастанию id.

# Выведете имена сотрудников, получившие нечетное id.

# Решить с помощью zip,filter,lambda

import random
arr1 = [random.randint(1, 100) for i in range(10)]
arr2 = ['Max', 'Andrew', 'Victor', 'Olga', 'Svetlana', 'Ivan', 'Daria', 'Alexander', 'Maria', 'Sergey']
print(arr1)
print(arr2)

arr = list(zip(arr1, arr2))
print(arr)

print(sorted(arr))

print(list(filter(lambda x: x[0]%2 != 0, arr)))

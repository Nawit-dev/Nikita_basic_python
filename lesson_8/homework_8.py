# ++++++++++++++++++++++++++++++++++++++++++++++++
# Задачи по итераторам
# ++++++++++++++++++++++++++++++++++++++++++++++++

# 1
myList = ['lorem', 1, 2,'test']
result = iter(myList)
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# 2
str = 'Москва'
result = iter(str)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# ++++++++++++++++++++++++++++++++++++++++++++++++
# Задачи по теме "Генераторы списков (List Comprehensions)"
# ++++++++++++++++++++++++++++++++++++++++++++++++

# 1
n = 25
result = [num ** 2 for num in range(1,n+1) ]
print(result)

# 2

result = [f'{i}' if i % 2 == 0 else f'{i}' for i in range(-10, 10+1)]
print(result)

# 3

words = ["лампа", "вихрь", "арбуз", "станок", "облако", "карандаш", "туман", "парус", "шкаф", "гроза"]
lenWordsList = [int(f'{len(words[i])}') for i in range(len(words))]
print(lenWordsList)

# 4

myList = [f'{i} - четное' if i % 2 == 0 else f'{i} - нечетное' for i in range(1, 20)]
print(myList)

# 5

objects = [42, "Hello", [1, 2, 3]]
is_iterable = [True if hasattr(obj, '__iter__') else False for obj in objects]
for i in range(len(objects)):
    print("Объект", objects[i], ":", "итерируемый" if is_iterable[i] else "не итерируемый")
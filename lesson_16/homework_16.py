# ++++++++++++++++++++++++++++++++++++++++++++++++
# Выражения-генераторы
# ++++++++++++++++++++++++++++++++++++++++++++++++

import random

# 1. Только строки из списка
data = ["Python", 123, "Java", 456, "C++", 789]

print(" ".join((x for x in data if isinstance(x, str))))

# 2. 10 случайных чисел и максимум
nums2 = list((random.randint(1, 100) for _ in range(10)))

print("Максимальное число:", max(nums2))

# 3. Слова длиннее 5 символов
words_content = "apple banana cat elephant python"

print(" ".join((w for w in words_content.split() if len(w) > 5)))

# 4. Строки с "Python"
text_content = """Hello world
Python is great
I love coding in Python
Java is also good"""

print("\n".join((line for line in text_content.splitlines() if "Python" in line)))

# 5. Бесконечный генератор до 50
def gen5():
    while True:
        num = random.randint(1, 100)
        yield num
        if num == 50:
            break

print(" ".join((str(x) for x in gen5())))

# 6. Первые N простых чисел
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

def gen6(n):
    num = 2
    while n:
        if is_prime(num):
            yield num
            n -= 1
        num += 1

print(" ".join((str(x) for x in gen6(10))))

# 7. Имитация загрузки данных
def gen7():
    i = 1
    while True:
        yield f"Получены данные {i}"
        i += 1

print("\n".join((next(gen7()) for _ in range(5))))

# 8. Квадраты чисел (генератор вместо map)
nums = (int(x) for x in "1 2 3 4 5".split())
print([x**2 for x in nums])

# 9. Города в верхнем регистре
cities = ["Москва", "Санкт-Петербург", "Казань"]
print([c.upper() for c in cities])

# 10. Числа делящиеся на 3 и 5
lst10 = [15, 30, 45, 22, 60, 77, 90, 100]
print([x for x in lst10 if x % 3 == 0 and x % 5 == 0])

# 11. Строки содержащие цифры
lst11 = ["hello", "world42", "python3", "abc", "123", "data1science"]
print([s for s in lst11 if any(c.isdigit() for c in s)])

# 12. Словарь страна → столица (через генератор словаря)
countries = ["Россия", "Франция", "Германия"]
capitals = ["Москва", "Париж", "Берлин"]
print({c: k for c, k in ((countries[i], capitals[i]) for i in range(len(countries)))})

# 13. Распаковка списка кортежей
data13 = [(1, 'a'), (2, 'b'), (3, 'c')]
nums13 = [x for x, _ in data13]
chars13 = [y for _, y in data13]
print(nums13)
print(chars13)

# 14. Сортировка имён
names = ["петр", "Иван", "мария", "Анна"]
print(sorted((x for x in names), key=lambda x: (x[0].islower(), x)))

# Сортировка товаров по цене
products = [("Телефон", 500), ("Ноутбук", 1000), ("Планшет", 700)]
print(sorted((p for p in products), key=lambda x: x[1]))
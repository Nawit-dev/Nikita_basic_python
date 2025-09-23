# ===============================================
# ЛЯМБДА-ФУНКЦИИ
# ===============================================

# 1. Квадрат числа
square = lambda x: x ** 2
print(square(5))  # пример

# 2. Проверка четности
is_even = lambda x: x % 2 == 0
print(is_even(4))
print(is_even(7))

# 3. Сортировка списка строк по последней букве
def sort_by_last_letter(words):
    return sorted(words, key=lambda x: x[-1])

words = ["banana", "apple", "cherry"]
print(sort_by_last_letter(words))


# ===============================================
# ЗАМЫКАНИЯ
# ===============================================

# 1. Функция умножения на n
def multiply_by(n):
    def inner(x):
        return x * n
    return inner

times3 = multiply_by(3)
times5 = multiply_by(5)
print(times3(10))  # 30
print(times5(10))  # 50

# 2. Счетчик с использованием nonlocal
def counter(start=0):
    count = start
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

c1 = counter(5)
c2 = counter()
print(c1())  # 6
print(c1())  # 7
print(c2())  # 1
print(c2())  # 2
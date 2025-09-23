# ===============================================
# ФУНКЦИИ
# ===============================================

# 1. Приветствие
def greet(name):
    print(f"Привет, {name}! Добро пожаловать!")

greet("Анна")

# 2. Квадрат числа
def square(num):
    return num ** 2

print(square(5))

# 3. Проверка четности
def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(7))

# 4. Повторение строки
def repeat_string(text, times):
    return text * times

print(repeat_string("Python", 3))

# 5. Сумма двух чисел
def add(a, b):
    return a + b

print(add(3, 7))

# 6. Максимум из трех чисел
def get_max(a, b, c):
    return max(a, b, c)

print(get_max(10, 25, 7))

# 7. Калькулятор
def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return None

print(calculate(10, 5, "+"))
print(calculate(10, 5, "*"))

# 8. Обратная строка
def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))

# 9. Сравнение строк с параметрами
def compare_strings(s1, s2, ignore_case=True, ignore_spaces=True):
    if ignore_spaces:
        s1 = s1.replace(" ", "")
        s2 = s2.replace(" ", "")
    if ignore_case:
        s1 = s1.lower()
        s2 = s2.lower()
    return s1 == s2

print(compare_strings("Hello", " hello "))
print(compare_strings("Hello", "HELLO", ignore_case=False))
print(compare_strings("Hello ", "Hello", ignore_spaces=False))

# 10. Суммирование чисел
def summarize(*args):
    return sum(x for x in args if isinstance(x, (int, float)))

print(summarize(1, 2, 3))
print(summarize(10, "abc", 5, 2))

# 11. Профиль пользователя
def create_profile(name, age, **extra):
    print("Профиль пользователя:")
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    if extra:
        print("Дополнительная информация:")
        for k, v in extra.items():
            print(f"{k}: {v}")

create_profile("Иван", 30, city="Москва", job="Инженер")

# 12. Обработка заказов со скидкой
def process_orders(*orders, discount=0):
    total = sum(orders)
    total_discounted = total * (1 - discount / 100)
    print(f"Сумма заказа: {total}")
    print(f"С учетом скидки: {total_discounted}")

process_orders(100, 200, 300, discount=10)

# 13. Объединение списков
def merge_lists(*lists):
    result = []
    for lst in lists:
        result.extend(lst)
    return result

print(merge_lists([1, 2], [3, 4], [5, 6]))

# 14. Объединение словарей
def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}
print(merge_dicts(d1, d2, d3))

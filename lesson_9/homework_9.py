# ===============================================
# СЛОВАРИ
# ===============================================

# 1. Словарь фруктов
fruits = {"яблоко": 100, "банан": 120, "груша": 150}
fruits["апельсин"] = 130
print("1.", fruits)

# 2. Студенты с оценкой >= 4
grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
print("2.", [name for name, grade in grades.items() if grade >= 4])

# 3. Столица страны
countries = {"Россия": "Москва", "Франция": "Париж", "Германия": "Берлин"}
country = input("3. Введите страну: ")
print(countries.get(country, "Страна не найдена"))

# 4. Студенты по курсам
students_list = [
    ("Анна", "Python"),
    ("Борис", "Java"),
    ("Виктор", "Python"),
    ("Галина", "C++"),
    ("Дмитрий", "Python")
]
courses = {}
for name, course in students_list:
    courses.setdefault(course, []).append(name)
print("4.", courses)

# 5. Удаление студента с самой низкой оценкой
grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
lowest = min(grades, key=grades.get)
grades.pop(lowest)
print("5.", grades)

# 6. Преобразование списка студентов в словарь с None и добавление возраста
students_names = ["Анна", "Борис", "Виктор", "Галина"]
students_dict = dict.fromkeys(students_names, None)
students_dict.update({"Анна": 20, "Борис": 22, "Виктор": 21, "Галина": 23})
print("6.", students_dict)

# 7. Курс валют
exchange_rates = {"USD": 90, "EUR": 98, "GBP": 115}
currency = input("7. Введите валюту: ")
if currency in exchange_rates:
    print(exchange_rates[currency])
else:
    print("Неизвестная валюта")
    exchange_rates[currency] = None
print(exchange_rates)

# 8. Объединение словарей
dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
dict1.update(dict2)
print("8.", dict1)


# ===============================================
# КОРТЕЖИ
# ===============================================

# 1. Кортеж из разных типов
t = (10, "строка", 3.14, True, [1, 2, 3])
print("Кортеж 1:", t[1], t[-1])

# 2. Количество вхождений и индекс
nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
print("Кортеж 2: count 4 =", nums.count(4), ", index 7 =", nums.index(7))

# 3. Преобразование списка в кортеж
lst = ["Python", "Java", "C++", "JavaScript"]
t3 = tuple(lst)
print("Кортеж 3: есть ли 'C++'? ", "C++" in t3)

# 4. Срезы кортежа
t4 = tuple(range(1, 11))
print("Кортеж 4: первые 3 =", t4[:3], ", последние 3 =", t4[-3:], ", шаг 2 =", t4[::2])

# 5. Вложенный список и словарь
t5 = ([1, 2, 3], {"a": 1, "b": 2})
t5[0].append(4)
print("Кортеж 5:", t5)

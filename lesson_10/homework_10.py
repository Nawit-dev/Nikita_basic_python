# ===============================================
# МНОЖЕСТВА
# ===============================================

# 1. Создание множества и добавление элементов
s1 = {1, 2, 3, 4}
s1.add(5)
s1.add(3)  # уже существует, изменений не будет
print("Множество 1:", s1)

# 2. Множество из списка городов
cities = ["Москва", "Париж", "Лондон", "Москва", "Берлин", "Париж"]
cities_set = set(cities)
print("Множество городов:", cities_set)
print("Количество уникальных городов:", len(cities_set))

# 3. Множество чисел от 1 до 10 и удаление элементов
numbers = set(range(1, 11))
numbers.discard(5)   # безопасное удаление
numbers.discard(15)  # безопасное удаление, числа нет
print("Множество после удаления:", numbers)

# 4. Множество символов строки
word = "abrakadabra"
letters = set(word)
print("Множество букв:", letters)
print("Количество различных букв:", len(letters))

# 5. Добавление разных типов в множество
s2 = set()
s2.add(10)
s2.add("hello")
s2.add((1, 2, 3))
# s2.add([4, 5, 6])  # ошибка, список не хэшируемый
print("Множество после добавления:", s2)
print("Список нельзя добавить, потому что он изменяемый и не хэшируемый")

# 6. Операции с множествами
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Пересечение A & B:", A & B)
print("Объединение A | B:", A | B)
print("Разность A - B:", A - B)
print("Разность B - A:", B - A)
print("Симметричная разность A ^ B:", A ^ B)

# 7. Четные и нечетные числа
even_numbers = set(range(2, 11, 2))
odd_numbers = set(range(1, 11, 2))
print("Пересечение четные & нечетные:", even_numbers & odd_numbers)
print("Объединение четные | нечетные:", even_numbers | odd_numbers)

# 8. Студенты на курсах
python_students = {"Анна", "Иван", "Мария", "Сергей"}
java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
print("На оба курса:", python_students & java_students)
print("Только на один курс:", python_students ^ java_students)
print("Хотя бы на один курс:", python_students | java_students)

# 9. Множества букв из слов
text1 = set("программирование")
text2 = set("автоматизация")
print("Общие буквы:", text1 & text2)
print("Только в первом слове:", text1 - text2)
print("Уникальные буквы каждого слова:", text1 ^ text2)


# ===============================================
# ГЕНЕРАТОРЫ МНОЖЕСТВ И СЛОВАРЕЙ
# ===============================================

# 1. Квадраты четных чисел от 1 до 10
squares_even = {x**2 for x in range(1, 11) if x % 2 == 0}
print("Квадраты четных чисел:", squares_even)

# 2. Уникальные слова в верхнем регистре
words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
unique_upper = {word.upper() for word in words}
print("Уникальные слова в верхнем регистре:", unique_upper)

# 3. Новый словарь по оценкам
grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
grades_eval = {k: ("отлично" if v >= 80 else "удовлетворительно") for k, v in grades.items()}
print("Оценки с описанием:", grades_eval)

# 4. Длина слов из множества
text = {"Python", "automation", "programming", "testing"}
length_dict = {word: len(word) for word in text}
print("Длина слов:", length_dict)

# 5. Вложенный словарь с множествами квадратов
n = 10
nested_dict = {i: {j**2 for j in range(1, i+1)} for i in range(1, n+1)}
print("Вложенный словарь с множествами квадратов:", nested_dict)

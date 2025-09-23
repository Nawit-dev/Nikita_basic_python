# Цикл while
# 1. Вывод чисел от 1 до N
N = int(input("Введите число N: "))
i = 1
while i <= N:
    print(i)
    i += 1

# 2. Сумма четных чисел до N
N = int(input("Введите число N: "))
i = 1
total = 0
while i <= N:
    if i % 2 == 0:
        total += i
    i += 1
print("Сумма четных чисел:", total)
#
# 3. Подсчет количества цифр в числе
num = int(input("Введите число: "))
count = 0
temp = num
while temp > 0:
    temp //= 10
    count += 1
print("Количество цифр:", count)

# 4. Определение максимальной цифры в числе
num = int(input("Введите число: "))
max_digit = 0
temp = num
while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
    temp //= 10
print("Наибольшая цифра:", max_digit)

# 5. Запрос пароля
while True:
    password = input("Введите пароль: ")
    if password == "qwerty123":
        print("Доступ разрешен")
        break

# Операторы break, continue и else
# 1. Поиск первого четного числа
numbers = [1, 3, 7, 4, 9]
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        print("Первое четное число:", numbers[i])
        break
    i += 1
else:
    print("Четное число не найдено")
#
# 2. Пропуск отрицательных чисел
# total = 0
while True:
    s = input("Введите число (0 для выхода): ")
    if s.strip() == '':
        continue
    num = int(s)
    if num == 0:
        break
    if num < 0:
        continue
    total += num
print("Сумма положительных чисел:", total)
#
# 3. Вывод нечетных чисел из диапазона
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
i = a
while i <= b:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
#
# 4. Проверка на простое число
N = int(input("Введите число N: "))
if N <= 1:
    print("Число не является простым")
else:
    i = 2
    while i < N:
        if N % i == 0:
            print("Число не простое")
            break
        i += 1
    else:
        print("Число простое")
#
# 5. Поиск максимального числа
max_num = None
while True:
    s = input("Введите число (0 для выхода): ")
    if s.strip() == '':
        break
    num = int(s)
    if num == 0:
        break
    if max_num is None or num > max_num:
        max_num = num
print("Максимальное число:", max_num)

# Цикл for
# 1. Вывести все символы строки в обратном порядке
s = input("Введите строку: ")
for c in s[::-1]:
    print(c, end='')
print()

# 2. Замена четных элементов списка на 0
lst = [1, 2, 3, 4, 5, 6]
for i in range(len(lst)):
    if lst[i] % 2 == 0:
        lst[i] = 0
print(lst)

# 3. Генерация списка степеней двойки
N = int(input("Введите число N: "))
powers = []
for i in range(N + 1):
    powers.append(2 ** i)
print(powers)

# 4. Вывод всех чисел от A до B с шагом K
A = int(input("Введите A: "))
B = int(input("Введите B: "))
K = int(input("Введите K: "))
for i in range(A, B + 1, K):
    print(i)
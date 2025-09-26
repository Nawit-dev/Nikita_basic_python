# Чтение и запись данных из файлов
# 1
f = open("data.txt", "r", encoding="utf-8")
print(f.read())
f.close()

# 2
f = open("data.txt", "r", encoding="utf-8")
print(f.readline(), end="")
f.close()

# 3
f = open("data.txt", "r", encoding="utf-8")
print(f.read(10))
f.close()

# 4
f = open("data.txt", "r", encoding="utf-8")
lines = f.readlines()
print(lines)
f.close()

# 5
f = open("data.txt", "r", encoding="utf-8")
for line in f:
    print("Строка:", line.strip())
f.close()

# 6
f = open("data.txt", "r", encoding="utf-8")
print(f.read(6))
print(f.read(6))
f.close()

# 7
import os

size = os.path.getsize("data.txt")
print("Размер файла:", size, "байт")

# 8
with open("data.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 9
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Ошибка: Файл не найден")

# 10
try:
    f = open("data.txt", "r", encoding="utf-8")
    print(f.read())
finally:
    f.close()

# 11
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("Ошибка: Файл не найден")

# 12
try:
    with open("numbers.txt", "r", encoding="utf-8") as f:
        total = 0
        for line in f:
            total += int(line.strip())
    print("Сумма:", total)
except FileNotFoundError:
    print("Ошибка: Файл не найден")

# 13
import datetime

with open("log.txt", "a", encoding="utf-8") as f:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"{now} Запуск программы\n")
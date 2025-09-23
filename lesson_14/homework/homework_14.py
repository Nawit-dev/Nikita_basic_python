# ===============================================
# МОДУЛИ В PYTHON
# ===============================================

# # 1. Импорт sqrt и pow из math
from math import sqrt, pow

print(sqrt(64))   # 8.0
print(pow(5, 3))  # 125.0

# # 2. Модуль random
import random

print("Случайное число:", random.randint(1, 10))
print("Выбранный язык:", random.choice(["Python", "Java", "C++"]))

import my_module

print(my_module.add(3, 5))
print(my_module.multiply(4, 6))

# 5. Измерение времени выполнения кода
import time

start = time.time()
time.sleep(2)
end = time.time()
print(f"Код выполнялся {end - start:.4f} сек")

# 6. Использование requests

import requests
response = requests.get("https://api.github.com")
print(response.status_code)

# 7. Построение графика с matplotlib

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]
plt.plot(x, y, marker='o')
plt.title("Пример графика")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
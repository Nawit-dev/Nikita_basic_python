# 4. Импорт из другого модуля
from utils import greet
greet("Алексей")

# 9. Создание простого пакета
from math_operations.addition import add
from math_operations.subtraction import subtract
print(add(5, 3))
print(subtract(10, 4))
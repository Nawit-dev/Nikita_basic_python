# 1
items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
result = list(filter(lambda x: isinstance(x, (str, list)), items))
print(result)  # ['hello', [1, 2], 'world']


# 2
def describe_type(x):
    if isinstance(x, str):
        print("Это строка")
    elif isinstance(x, (int, float)):
        print("Это число")
    elif isinstance(x, bool):
        print("Это булевое значение")
    else:
        print("Неизвестный тип")

describe_type(5.5)
describe_type(True)
describe_type("Привет")
describe_type([1, 2, 3])


# 3
from typing import Callable

def filter_list(f: Callable[[int], bool], data: list[int]) -> list[int]:
    return list(filter(f, data))

print(filter_list(lambda x: x > 3, [1, 3, 5, 7]))  # [5, 7]


# 4
def print_info(name: str, age: int, tags: list[str]) -> None:
    print(name, age, tags)


# 5
def analyze(data: list[float]) -> None:
    if data:
        print("Количество элементов:", len(data))
        print("Среднее значение:", sum(data) / len(data))
    else:
        print("Список пустой")

analyze([1, 2, 3, 4, 5])
analyze([])


# 6
flags = [True, True, True, False]
print(all(flags))  # False
print(any(flags))  # True


# 7. Победа по строке
field = ['x', 'x', 'x', 'o', 'o', '', '', '', '']
print(all(cell == 'x' for cell in field[0:3]))  # True


# 8
P = ['0', '0', '0', '*', '0']
print(any(cell == '*' for cell in P))  # True


# 9
import random

colors = ["red", "green", "blue", "yellow", "purple"]
print("Выбран цвет:", random.choice(colors))


# 10
random.seed(42)
nums = [random.randint(0, 100) for _ in range(10)]
print(nums)


# 11
def greet(name: str) -> str:
    return f"Привет, {name}!"

print(greet("Анна"))


# 12
def multiply(a: float, b: float) -> float:
    return a * b

print(multiply(4, 5))  # 20


# 13
def area(length: float, width: float) -> float:
    return length * width

print(area.__annotations__)

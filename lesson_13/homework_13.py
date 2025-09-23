import time
from functools import wraps

# ===============================================
# ДЕКОРАТОРЫ
# ===============================================

# 1. Декоратор для верхнего регистра
def uppercase_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello, world!"

print(say_hello())  # "HELLO, WORLD!"


# 2. Декоратор повторения n раз
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello!")

hello()


# 3. Декоратор кэширования
def cache(func):
    cached_results = {}
    @wraps(func)
    def wrapper(*args):
        if args in cached_results:
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper

@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b

print(slow_add(2, 3))  # Вычисляю 2 + 3... 5
print(slow_add(2, 3))  # 5 (из кэша)


# 4. Декоратор с таймером
def timer(repeat_count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            times = []
            for _ in range(repeat_count):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                times.append(end - start)
            avg_time = sum(times) / repeat_count
            print(f"Среднее время выполнения: {avg_time:.4f} сек")
        return wrapper
    return decorator

@timer(3)
def slow_function():
    time.sleep(1)

slow_function()
# Задание 5. Напишите функцию для вычисления значения выражения (a+4b)(a−3b)+a2;
import random


def task5(a, b):
    result = (a + (4 * b)) * (a - (3 * b)) + (a * 2)
    return result


print(task5(3, 2))
print(task5(random.randint(1, 100), random.randint(1, 100)))
print()

for i in range(5):
    for j in range(5):
        print(f'{task5(i, j)} (a = {i}, b = {j})\t', end='')
    print()

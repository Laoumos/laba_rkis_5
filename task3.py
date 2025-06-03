# Задание 3. Сформируйте возрастающий массив из случайных четных чисел;

import random
cap = 100
length = 10
print(sorted([random.randint(0, (int(cap / 2)) * 2) for i in range(length)], key=None, reverse=False))

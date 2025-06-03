# Задание 1. Посчитайте сумму целых чисел, расположенных между числами 1 и N
# включительно;
user_input = int(input('\t 1 + ... + N\nВведите число N: '))
result = 0
if user_input != 1:
    for i in range(1, user_input + 1):
        result += i
print(f'Результат есть {result}')
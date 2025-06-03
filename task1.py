# Задание 1. Посчитайте сумму целых чисел, расположенных между числами 1 и N
# включительно;
user_input = int(input('\t 1 + ... + N\nВведите число N: '))
if user_input:
    for i in range(1, user_input):
        user_input += i
print(f'Результат есть {user_input}')

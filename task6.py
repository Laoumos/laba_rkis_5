# Задание 6. Дан массив, содержащий положительные и отрицательные числа. Замените
# все элементы массива на противоположные по знаку. Например, задан массив [1, -5, 0, 3,
# -4], после преобразования должно получиться [-1, 5, 0, -3, 4];

def turn_the_tables(array):
    for i in range(len(array)):
        k = array[i] * 2
        array[i] -= k
    return array

test = [1, -5, 0, 3, -4]
test2 = [1, -8, 0, -1.5, 4.5, -6]

print(f'{test} --> {turn_the_tables(test)}')
print(f'{test2} --> {turn_the_tables(test2)}')

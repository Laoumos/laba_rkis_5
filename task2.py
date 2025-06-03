# Задание 2. Петя успевает по математике лучше всех в классе, поэтому учитель задал ему
# сложное домашнее задание, в котором нужно в заданном наборе целых чисел найти сумму
# всех положительных элементов, затем найти где в заданной последовательности
# находятся максимальный и минимальный элемент и вычислить произведение чисел,
# расположенных в этой последовательности между ними. Так же известно, что
# минимальный и максимальный элемент встречаются в заданном множестве чисел только
# один раз и не являются соседними. Напишите функцию, которая примет массив и вернет
# два числа (сумму положительных элементов и произведение чисел, расположенных между
# минимальным и максимальным элементами);

import random

def petya(array):
    # решение на сумму элементов
    result_sum = 0
    only_positives = [i for i in array if i > 0]
    for i in range(len(only_positives)):
        result_sum += only_positives[i]

    # решение на произведение чисел
    array_maxnum = array[0]
    array_minnum = array[0]
    max_index = 0
    min_index = 0
    result_multiply = 1

    for i in range(len(array)):
        if array[i] > array_maxnum:
            array_maxnum = array[i]
            max_index = i
        if array[i] < array_minnum:
            array_minnum = array[i]
            min_index = i

    if max_index - min_index == 1 or min_index - max_index == 1:
        result_multiply = None
    else:
        if max_index < min_index:
            for i in range(max_index + 1, min_index):
                    result_multiply *= array[i]
        if max_index > min_index:
            for i in range(min_index + 1, max_index):
                    result_multiply *= array[i]

    return result_sum, result_multiply, max_index, min_index


test = [1, -4, 3, 4, 5, -4, 1, -2, -3]
test2 = [random.randint(-100, 100) for i in range(10)]
print(petya(test), test)
print(petya(test2), test2)


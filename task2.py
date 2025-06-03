# Задание 2. Петя успевает по математике лучше всех в классе, поэтому учитель задал ему
# сложное домашнее задание, в котором нужно в заданном наборе целых чисел найти сумму
# всех положительных элементов, затем найти где в заданной последовательности
# находятся максимальный и минимальный элемент и вычислить произведение чисел,
# расположенных в этой последовательности между ними. Так же известно, что
# минимальный и максимальный элемент встречаются в заданном множестве чисел только
# один раз и не являются соседними. Напишите функцию, которая примет массив и вернет
# два числа (сумму положительных элементов и произведение чисел, расположенных между
# минимальным и максимальным элементами);

def petya(array):
	# решение на сумму элементов
	result_sum = 0
	only_positives = [i for i in array if i > 0]
	for i in range(len(only_positives)):
		result_sum += only_positives[i]

	# решение на произведение чисел
	array_maxnum = array[0]
	array_minnum = array[0]
	result_multiply = 1

	for i in range(len(array)):
		if array[i] > array_maxnum:
			array_maxnum = array[i]
		if array[i] < array_minnum:
			array_minnum = array[i]

	for i in range(array.index(array_maxnum) + 1, array.index(array_minnum)):
		result_multiply *= array[i]

	return result_sum, result_multiply


test = [1, 2, 3, 4, 5, -1, -2, 4, -3]
print(petya(test), test)
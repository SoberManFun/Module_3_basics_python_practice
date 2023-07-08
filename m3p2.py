#___________________МОДУЛЬ_3_ЧАСТЬ_2_УРОВЕНЬ1_НАЧАЛО____________________
# def list_repeat(l):
# 	repeat1 = []
# 	for i in range(len(l)):
# 		if l[i] in l[i+1:] and l[i] not in repeat1:
# 			repeat1.append(l[i])
# 	return(repeat1)

# l = [1,4,1,6,"hello","a","hello",1,5,1,4,4]
# repeat2 = list_repeat(l)
# print(repeat2)
#___________________МОДУЛЬ_3_ЧАСТЬ_2_УРОВЕНЬ1_КОНЕЦ_____________________

#___________________МОДУЛЬ_3_ЧАСТЬ_2_УРОВЕНЬ2_НАЧАЛО____________________
# def find_max(matrix):
# 	max_element = matrix[0][0]
# 	for row in matrix:
# 		for element in row:
# 			if element > max_element:
# 				max_element = element
# 	return max_element

# from random import randint
# n = int(input('Введите разрядность матрицы: '))
# d = int(input('Введите диапазон значений матрицы: '))
# m = [[randint(0, d) for i in range(n)] for j in range(n)]
# print('Сгенерирована следующая матрица: ')
# for row in m:
# 	print(row)
# max_element = find_max(m)
# print("Максимальный элемент матрицы:", max_element)
#___________________МОДУЛЬ_3_ЧАСТЬ_2_УРОВЕНЬ2_КОНЕЦ_____________________

#___________________МОДУЛЬ_3_ЧАСТЬ_2_УРОВЕНЬ3_НАЧАЛО____________________
# def swap_keys_values(dictionary):
# 	swapped_dict = {value: key for key, value in dictionary.items()}
# 	return swapped_dict

# my_dict = {"name1": "id1", "name2": "id2", "name3": "id3"}
# swapped_dict = swap_keys_values(my_dict)
# print("Исходный словарь:", my_dict)
# print("Измененный словарь:", swapped_dict)
#___________________МОДУЛЬ_3_ЧАСТЬ_2_УРОВЕНЬ3_КОНЕЦ_____________________
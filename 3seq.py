# МОДУЛЬ 3

"""
Задание:
Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
"""

# Получаем строку с цифрами и разделителями 1-го списка
dig_list_1 = input('Введите цифры 1-го списка через разделитель ("," ";" "/"): ')

# Формируем 1-й список из строки, используя разные разделители
if dig_list_1[1] == ',':
    digit_list_1 = dig_list_1.split(sep=',')
elif dig_list_1[1] == ';':
    digit_list_1 = dig_list_1.split(sep=';')
elif dig_list_1[1] == '/':
    digit_list_1 = dig_list_1.split(sep='/')
print(digit_list_1)

# Получаем строку с цифрами и разделителями 2-го списка
dig_list_2 = input('Введите цифры 2-го списка через разделитель ("," ";" "/"): ')

# Формируем 2-й список из строки, используя разные разделители
if dig_list_2[1] == ',':
    digit_list_2 = dig_list_2.split(sep=',')
elif dig_list_2[1] == ';':
    digit_list_2 = dig_list_2.split(sep=';')
elif dig_list_2[1] == '/':
    digit_list_2 = dig_list_2.split(sep='/')
print(digit_list_2)

# Формируем список из уникальных элементов 2-го списка
unique_list = list(set(digit_list_2))

# Удаляем уникальные элементы 2-го списка из 1-го списка
for digit in unique_list:
    if digit_list_1.count(digit) != 0:
        for i in range(digit_list_1.count(digit)):
            digit_list_1.remove(digit)

# Выводим на экран 1-й список без элементов 2-го списка
print('\nОТВЕТ: элементы второго списка удалены из первого списка')
for i in range(len(digit_list_1)):
    if i != len(digit_list_1) - 1:
        print(digit_list_1[i], end=',')
    else:
        print(digit_list_1[i])

# #Разделить строку
# my_string = "Пример строки для разделения"
# parts = my_string.split()  # Разделение по пробелу
# print(parts)  # Выведет: ['Пример', 'строки', 'для', 'разделения']
#
#Как найти индекс символа в строке
# salamaleykum = "Hello, NIggaz"
# index = salamaleykum.index("o")
# print(index)
#
#Объединить строки
# strings = ["Привет", "мир"]
# result = " ".join(strings)  # Объединение строк из списка с пробелом между ними
# print(result)  # Выведет: "Привет мир"
#
# name = "John"
# age = 30
# result = f"Привет, меня зовут {name} и мне {age} лет."
# print(result)  # Выведет: "Привет, меня зовут John и мне 30 лет."
# # or just '+'
#
#Заменить часть строки
# my_string = "Это пример строки"
# new_string = my_string.replace("пример", "новый пример")
# print(new_string)  # Выведет: "Это новый пример строки"
#
#Удалить пробелы в строке
# my_string = "Это строка с пробелами"
# new_string = my_string.replace(" ", "")  # Удаление всех пробелов из строки
# print(new_string)  # Выведет: "Этострокаспробелами"
#
# my_string = "   строка с пробелами   "
# new_string = my_string.strip()  # Удаление пробелов с обоих концов строки
# print(new_string)  # Выведет: "строка с пробелами"
#
# my_string = "   строка с пробелами   "
# left_stripped = my_string.lstrip()  # Удаление пробелов слева
# right_stripped = my_string.rstrip()  # Удаление пробелов справа
# print(left_stripped)  # Выведет: "строка с пробелами   "
# print(right_stripped)  # Выведет: "   строка с пробелами"
#
#Удалить символы в строке
# my_string = "Это строка с символами"
# new_string = my_string.replace("с", "")  # Удаление символа "с" из строки
# print(new_string)  # Выведет: "Это трока иимволами"
#
# my_string = "Это строка с символами"
# chars_to_remove = ['с', 'и']
# new_string = "".join(char for char in my_string if char not in chars_to_remove)  # Удаление символов "с" и "и"
# print(new_string)  # Выведет: "Это трока  символам"

#Удалить последний символ в строке
# my_string = "Пример строки для удаления последнего символа"
# new_string = my_string[:-1]  # Удаление последнего символа с помощью среза
# print(new_string)  # Выведет: "Пример строки для удаления последнего символ"
#
# my_string = "Пример строки для удаления последнего символа"
# new_string = my_string.rstrip(my_string[-1])  # Удаление последнего символа с помощью метода rstrip()
# print(new_string)  # Выведет: "Пример строки для удаления последнего символ"
#
#Удалить первый символ в строке
# my_string = "Пример строки для удаления первого символа"
# new_string = my_string[1:]  # Удаление первого символа с помощью среза
# print(new_string)  # Выведет: "ример строки для удаления первого символа"
#
# my_string = "Пример строки для удаления первого символа"
# new_string = my_string.lstrip(my_string[0])  # Удаление первого символа с помощью метода lstrip()
# print(new_string)  # Выведет: "ример строки для удаления первого символа"
#
# my_string = "Пример строки для удаления первого символа"
# new_string = my_string.replace(my_string[0], "", 1)  # Удаление первого символа с помощью метода replace()
# print(new_string)  # Выведет: "ример строки для удаления первого символа"
#
#Удалить строку
# my_string = "Это строка для удаления"
# del my_string  # Удаление переменной, содержащей строку
#
# my_string = "Это строка для удаления"
# my_string = None  # Присвоение переменной значения None

# #Найти символы в строке
# my_string = "Это строка для поиска символов"
# char_to_find = "о"
# if char_to_find in my_string:
#     print(f"Символ '{char_to_find}' найден в строке.")
# else:
#     print(f"Символ '{char_to_find}' не найден в строке.")
#
# my_string = "Это строка для поиска символов"
# char_to_find = "о"
# count = my_string.count(char_to_find)
# print(f"Символ '{char_to_find}' встречается {count} раз(а) в строке.")
#
#Количество символов в строке
# my_string = "Это строка с символами"
# length = len(my_string)
# print(length)  # Выведет: 20
#
#Посчитать количество определенных символов в строке
# my_string = "Это строка с символами"
# char_to_count = "о"
# count = my_string.count(char_to_count)
# print(f"Символ '{char_to_count}' встречается {count} раз(а) в строке.")
#
# my_string = "Это строка с символами"
# char_to_count = "о"
# count = sum(1 for char in my_string if char == char_to_count)
# print(f"Символ '{char_to_count}' встречается {count} раз(а) в строке.")
#
#Как сделать кортеж
# empty_tuple = ()
#
# my_list = [1, 2, 3, 4]
# tuple_from_list = tuple(my_list)
#
#Как объединить кортежи
# tuple1 = (1, 2, 3)
# tuple2 = ("a", "b", "c")
# tuple1 += tuple2
# print(tuple1)  # Выведет: (1, 2, 3, "a", "b", "c")
#
# #Как сравнить кортежи
# #== ><
#
#Как создать список
# empty_list = []
#
# my_tuple = (1, 2, 3, 4)
# list_from_tuple = list(my_tuple)
#
#Создать список циклом
# my_list = []
# for i in range(1, 11):
#     my_list.append(i)
# print(my_list)  # Выведет: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
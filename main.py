# first_name = input("Введите ваше имя:")
# last_name = input("Введите вашу фамилию:")
# age = input("Введите ваш возраст:")
# city = input("Введите город проживания:")
# # Выводим пустую строку
# print("")
#
# # Выводим приветствие, подставляя имя и фамилию пользователя,
# # которые он ввёл с клавиатуры
# print("Привет,", first_name, last_name, "!")
#
# # Выводим пустую строку
# print("")
#
# # Выводим фиксированный текст для удобства просмотра
# print("Ваш профиль:")
#
# # Выводим возраст и город, которые указал пользователь
# print("Возраст:", age)
# print("Город:", city)
# def unique_elements(seq1, seq2):
#     set1 = set(seq1)
#     set2 = set(seq2)
#     unique = list(set1.symmetric_difference(set2))  # Используется функция symmetric_difference
#     return unique

# Пример использования
# sequence1 = [1, 2, 3, 4, 5, 6, 7, 8]
# sequence2 = [2, 4, 6, 8, 10, 12]
# result = unique_elements(sequence1, sequence2)
# print(result)
# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))
shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print(list_id_after == list_id_before)
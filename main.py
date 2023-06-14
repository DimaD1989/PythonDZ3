# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
# import  collections
#
# new_list = [6, 6, 77, 8, 5, 5, 7, 8, 3, 3, 1, 2, 4, 100]
# duplicate_elements = {}
# for item in new_list:
#     if item in duplicate_elements:
#         duplicate_elements[item] += 1
#     else:
#         duplicate_elements[item] = 1
# print(duplicate_elements)
#
# new_list = [6, 6, 77, 8, 5, 5, 7, 8, 3, 3, 1, 2, 4, 100]
#
# count_frequency = collections.Counter(new_list)
# print(dict(count_frequency))
#
# new_list = [6, 6, 77, 8, 5, 5, 7, 8, 3, 3, 1, 2, 4, 100]
#
# count_frequency = filter(lambda  x: new_list.count(x)>1, new_list)
# count_frequency = list(set(new_list))
#
# print(count_frequency)
# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
#
# def most_frequent(text: str) -> list[str]:
#     dict_counts = {}
#     LIMIT = 10
#     new_sorted_dictionary = {}
#     new_text = text.replace(',', ''). \
#         replace('.', ''). \
#         replace('?', ''). \
#         replace('!', ''). \
#         replace('"', ''). \
#         lower(). \
#         strip()
#     words_list = new_text.split()
#     for word in words_list:
#         counter = words_list.count(word)
#         dict_counts[word] = counter
#     sorted_values = sorted(dict_counts.values())[::-1]
#     for i in sorted_values:
#         for j in dict_counts.keys():
#             if dict_counts[j] == i:
#                 new_sorted_dictionary[j] = dict_counts[j]
#     return list(new_sorted_dictionary.items())[0: LIMIT]
#
#
# text = 'HTTPS не является отдельным протоколом. Это обычный HTTP, работающий через шифрованные транспортные механизмы SSL и TLS. Он обеспечивает защиту от атак, основанных на прослушивании сетевого соединения — от снифферских атак и атак типа man-in-the-middle, при условии, что будут использоваться шифрующие средства и сертификат сервера проверен и ему доверяют.\
# По умолчанию HTTPS URL использует 443 TCP-порт (для незащищённого HTTP). Чтобы подготовить веб-сервер для обработки https-соединений, администратор должен получить и установить в систему сертификат открытого и закрытого ключа для этого веб-сервера. В TLS используется как асимметричная схема шифрования (для выработки общего секретного ключа), так и симметричная (для обмена данными, зашифрованными общим ключом).\ '
# print(most_frequent(text))


# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкз
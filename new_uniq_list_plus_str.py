def uniqueness(list):
    '''
    Напишите программу на Python, которая получает на вход список чисел и возвращает новый список,
    содержащий только уникальные элементы из исходного списка.
    Например, если исходный список выглядит так: [1, 2, 3, 2, 4, 3, 5],
    то программа должна вернуть новый список, содержащий только уникальные элементы: [1, 2, 3, 4, 5].
    '''
    empty_list = []
    for count_elem in range(len(list)):
        if list[count_elem] not in empty_list:
            empty_list.append(list[count_elem])
    return empty_list


list = [1, 2, 2, 3, 4, 3, 7] # [1, 2, 3, 4, 7]
print(uniqueness(list))

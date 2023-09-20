dict_one = {"one": [1, 2], "1.2": "13", "city": "windhook"}
dict_two = {"one": "14", "1.2": "13", "city": "germany"}
final_dict = {}
dict_one.copy(), dict_two.copy()
final_dict.update(dict_one), final_dict.update(dict_two)
if dict_one.keys() == dict_two.keys():
    for keys in dict_one.keys():
        if keys in dict_two:
            final_dict[keys] = dict_one[keys] + " " + dict_two[keys]

print(final_dict)


"""
Д/з
Объединение словарей: Напишите функцию, которая принимает несколько словарей
в качестве входных параметров и объединяет их в один словарь. Если ключи повторяются, значения объединяются.
"""


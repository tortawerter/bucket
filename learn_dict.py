#def(text_test):


punct = [".", ",", "?", "!", "…", ";", "-", ":", "\"", "\"", "\'", "\'", "(", ")", "[", "]"]
a = "hello alien hello''\", \""
for word in a:
    if word in punct:
        a = a.replace(word, "")
a = a.split()
text_dict = {}
for i in a:
    if i in text_dict:
        text_dict[i] += 1
    else:
        text_dict[i] = 1
print(max(text_dict.values()))
for n in text_dict.items():
    if n[1] == max(text_dict.values()):
        print(n[0])

print(a, text_dict)


# [".", ",", "?", "!", "…", ";", "-", ":", "\"", "\"", "\'", "\'", "(", ")", "[", "]"]

"""
Подсчет частоты встречаемости слов в тексте: Напишите функцию, которая принимает текст как входной
параметр и возвращает словарь, где ключами являются слова, а значениями - количество их вхождений в тексте.
"""

# information = ["имя: Тимофей", "фамилия: Быков", "рост: 175см", "вес: 61кг", "дата рождения: 20.03.2008"]
information = ["name: Timofey", "surname: Bykov", "height: 175sm"]

with open('test.txt', 'w') as test:
    for info in information:
        test.write(str(info) + '\n')

import random #импорт библиотек

a = list(range(12)) #вводится число
random.shuffle(a)# рандом
print(a)#принтуется число а, которое уже рандомное
for h in range(len(a) - 1): #что бы перенести все символы, команде надо повториться (len(a) - 1)
    for i in range(1, len(a)): #-------------------||------------------------------ ( 1, len(a)
        if a[i] < a[i - 1]: #сравнение числа и предшетвуещего ему
            a[i], a[i - 1] = a[i - 1], a[i] #если первое условие выполняется, то он меняет их местами
            print(a) #принтует каждую измененную строчку

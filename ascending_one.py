# import random

a = [1, 14, 5, 7, 10, 11, 12, 3, 16]
#random.shuffle(a)
#print(a)
for h in range(len(a) - 1):
    for i in range(len(a) - h - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            print(a)

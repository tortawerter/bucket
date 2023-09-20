import numpy as np


a = int(input("градусы: "))
b = a * (np.pi / 180)
print('радианы: ')
print(b)
print("проверка: ")
print(b * (180 / np.pi))

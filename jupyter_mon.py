import numpy as np
x = float(input('введите X: '))
for i in range(100):
    x += 0.1
    print(np.sqrt(np.cos(x)) * np.cos(200 * x) + np.sqrt(np.abs(x)) - (np.pi / 4) * (4 - x ** 2) ** 0.01, x)

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 5.001, 0.001)
y = x
y1 = 0 * x
x2 = [5, 5]
y2 = [0, 5]
# plt.plot(x, y, x, y1,"-g", x2, y2, "-r")
plt.legend(["a", "b", "c"])
plt.ylim([-1, 6])
plt.grid()
# plt.show()
print("Введите все известные данные.", "Если данных нет, то вводится ноль.")
a, b, c = 13, 12, 5
a_b, a_c = 1, 1

# map(int, input().split())
# def grad_rad(a_b, a_c):
#    a_b = a_b * (np.pi / 180)
#    a_c = a_c * (np.pi / 180)
#    return a_b, a_c



"""
a: 1, b: 1, c: 1 +
a: 1, b: 1, c: 0
a: 1, b: 0, c: 1
a: 1, b: 0, c: 0
a: 0, b: 0, c: 0
a: 0, b: 1, c: 1
a: 0, b: 0, c: 1
a: 0, b: 1, c: 0

a_b: 0, a_c: 0
a_b: 1, a_c: 1
a_b: 1, a_c: 0
a_b: 1, a_c: 1
"""
n = 0

a_f, a_j = 0, 0
if a != 0 and b != 0 and c != 0:
    for amount in range(91):
        while np.sin((amount * (np.pi / 180))*n) % 10 != 0:
            n += 10**n
            print(n, "yes")
        if np.sin(amount * (np.pi / 180) * n) == (c / a) * n:
            a_f += amount
            a_j += 90 - amount
    print(a_f, a_j)
    print((c/a) * n)




import math

a = 0
b = 1
for i in range(100):
    a += 1
    b += 1
    c = a / math.factorial(b)
    print(float(c))
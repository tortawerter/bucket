a = float(input("введите число: "))
b = float(input("введите изначальную степень: "))
for i in range(50000):
    b += 0.001
    c = a ** b
    print(c)

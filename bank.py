a = float(input("введите сумму: "))#сумма
b = float(input("введите проценты: "))#проценты
c = float(input("введите количество лет: "))#года


def bank(a, b, c):
    if c == 1:
        return a
    if c == 2:
        return a + a * (b / 100)
    if c == 3:
        return (a * (b + 100) ** 2) / 10000
    else:
        h = (a * (b + 100) ** 2 / 10000) * ((b + 100) ** (c - 3)) / (100 ** (c - 3))
        return h


print(bank(a, b, c))

polindrom = 99388 # 1234
reversed_num = 0

while polindrom > 0:
    reversed_num *= 10
    reversed_num += polindrom % 10
    polindrom //= 10

print(reversed_num)

import random

a = list(range(12))
s = []
random.shuffle(a)
print(a)
print(a[::-1])
i = 1
while True:
    count = len(a) - i
    i += 1
    s.append(a[count])
    if count == 0:
        break
print(s)

n = 0
while True:
    s = []
    for i in range(1, n+1):
        if n % i == 0:
            s.append(i)
    if len(s) >= 11 and s[3] * s[10] == n:
        print(s, len(s))
    n += 1

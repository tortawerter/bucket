n = 200
for i in range(200):
    n -=1
    a = n + (n - 1) + (n - 2) + (n - 3) + (n - 4) + (n - 5)
    b = (n - 6) + (n - 7) + (n - 8) + (n - 9) + (n - 10) + (n - 11) + (n - 12) + (n - 13) + (n - 14)
    if a - b == 0:
        print('yes')
        print(n)

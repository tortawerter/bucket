k, l, m, n = map(int, input().split())
if(k + l) % 2 == (m + n) % 2 == 0:
    print('yes')
else:
    print('no')

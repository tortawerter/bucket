a, b, c = (int, input('введите выражение: ' ).split())
type(a(int))
print(a, type(a))
if b == "*":
    print(a * c)
elif b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
elif b == "/":
    print(a / c)
elif b == "^" or b == "**":
    print(a ** c)
else:
    print('incorrect data')

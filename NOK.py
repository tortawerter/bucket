def NOK(num1, num2):
    n = 1
    if num2 > num1:
        num1, num2 = num2, num1
    if num1 % num2 == 0:
        return num1
    else:
        while (num1 * n) % num2 != 0:
            n += 1
    return num1 * n

test = [
    [12, 8],
    [8, 12],
    [3, 14],
    [8, 99],
    [1, 1],
]
num1, num2 = map(int, input().split())
print(NOK(num1, num2))
assert NOK(12, 8) == 24, "error1"
assert NOK(8, 12) == 24, "error2"
assert NOK(3, 14) == 42, "error3"
assert NOK(8, 99) == 792, "error4"
assert NOK(1, 1) == 1, "error5"


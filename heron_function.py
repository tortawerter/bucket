a, b, c = map(float, input().split())


def triangle_checker(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        return True
    else:
        return False


def heron_function(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s


if triangle_checker(a, b, c):
    print(heron_function(a, b, c))
else:
    print("This is not triangle")

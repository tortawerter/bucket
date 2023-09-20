a = int(input('введите количество углов: '))

def sumangle(a):
    answer = (a - 2) * 180
    if (a * a) == (a * -1) or a == 0 or a == 1 or a == 2:
        print('невозможно')
    return answer


print(sumangle(a))
a = float(input("введите сумму: "))#сумма
b = float(input("введите проценты: "))#проценты
c = float(input("введите количество лет: "))#года


def bank_two(a, b, c):
    return a * ((1 + b / 100) ** c)


print("summa: ", bank_two(a, b, c))



def output_one_bank(bank_two, a):
    return bank_two(a, b, c) - a #overprice


print("overprice: ", output_one_bank(bank_two, a))


def output_two_percentage(bank_two, output_one_bank):
    return (bank_two(a, b, c) / 100) * output_one_bank(bank_two, a) #percentage


print("percentage: ", output_two_percentage(bank_two, output_one_bank))

# 100, 110, 110 - 100 = 10 = ?% from 100
#output:1 over price, 2 percentage sootnoshenie
#factorial

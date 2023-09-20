def ReverseNumber(num_pol_rec):
    if num_pol_rec < 0:
        return 0
    elif num_pol_rec == 0:
        return 0
    counter = 0
    num_pol_2 = num_pol_rec
    while num_pol_2 > 0:
        num_pol_2 //= 10
        counter += 1
    last_num = num_pol_rec % 10
    ans = last_num * 10 ** (counter - 1)
    return ans + ReverseNumber(num_pol_rec // 10)



num_pol_rec = 1234
print(ReverseNumber(num_pol_rec))


"""
num_pol = int(input())
a = 0

while num_pol > 0:
    a *= 10
    a += num_pol % 10
    num_pol //= 10

print(a)
"""

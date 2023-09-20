num_min, num_max, num, num_sum = 0, 0, 1, 0
while num != 0:
    num = int(input())
    num_sum += num
    if num < 0:
        num_min += 1
    elif num > 0:
        num_max += 1
print(num_max - num_min, "\n", num_sum, sep="")

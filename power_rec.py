def PowerRec(num_power, power):
    if power <= 0:
        return 1
    else:
        return num_power * PowerRec(num_power, power - 1)


num_power = 3
power = 3

print(PowerRec(num_power, power))

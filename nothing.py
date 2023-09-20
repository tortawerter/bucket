day = int(input("дни: "))
n, total_temperature = 0, 0
result = ""
for i in range(day):
    temperature = int(input("температура: "))
    total_temperature += temperature
    div_eq = total_temperature / day
    if temperature > 0:
        n += 1
if n >= 5:
    result = "YES"
else:
    result = "NO"
print(div_eq, "\n\n", result, sep="")
# 86 // 8, 86 % 8
# 10, 75
a = int(input("введите число: ")) #4321
c = 0
while a > 1:
    c += 1
    a = a / 10 ** c
print(c + 1)
for i in range(1, c + 1):
    f = a // 10 ** (c - i) % 10
print(f)




#c = a % 10;
#4321; 4321 % 10 = 1; (4321 - 4321 % 10) / 10**1 % 10 = 2
#4321 / 10 = 432,1 - 432
#4321 = 4000 + 300 + 20 + 1 = 4 * 10**3 + 3 * 10**2 + 2 * 10**1 + 1 * 10**0
#1234 = 1000 + 200 + 30 + 4 = 1 * 10**3 + 2 * 10**2 + 3 * 10**1 + 4 * 10**0
# //; %; +; -; *; /; **;
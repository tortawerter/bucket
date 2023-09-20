def factorial(num_fact):
    ans = 1
    for i in range(1, num_fact + 1):
        ans *= i
    return ans


num_fact = int(input("введите число: "))

if num_fact < 0:
    print("ERROR")
else:
    print(factorial(num_fact))

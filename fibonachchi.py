def fibonacci(n):
    if n < 0:
        return "Error"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        previous_number = 1
        current_number = 1
        for _ in range(2, n):
            temp = current_number
            current_number = previous_number + current_number
            previous_number = temp
        return current_number

num = int(input("Введите номер числа Фибоначчи: "))

result = fibonacci(num)

print("Число Фибоначчи под номером", num, "равно", result)

num_fib = int(input())
def fibonachchi(num_fib):
    if num_fib <= 0:
        return 0
    elif num_fib == 1:
        return 1
    elif num_fib == 2:
        return 1
    else:
        return fibonachchi(num_fib - 1) + fibonachchi(num_fib - 2)


print(fibonachchi(num_fib))


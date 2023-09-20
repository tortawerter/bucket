def fibonachchi_cycle(num_fib):
    if num_fib < 0:
        return "error"
    elif num_fib == 0:
        return 0
    elif num_fib == 1:
        return 1
    elif num_fib == 2:
        return 1
    else:
        previos_num = 1
        current_num = 1
        for _ in range(2, num_fib):
            third_num = current_num
            current_num = previos_num + current_num
            previos_num = third_num
        return current_num


def fibonachchi_rec(num_fib):
    if num_fib < 0:
        return "error"
    elif num_fib == 0:
        return 0
    elif num_fib == 1:
        return 1
    elif num_fib == 2:
        return 1
    else:
        return fibonachchi_rec(num_fib - 1) + fibonachchi_rec(num_fib - 2)


assert fibonachchi_cycle(0) == fibonachchi_rec(0), "error1"
assert fibonachchi_cycle(5) == fibonachchi_rec(5), "error2"
assert fibonachchi_cycle(-1) == fibonachchi_rec(-1), "error3"
assert fibonachchi_cycle(000) == fibonachchi_rec(000), "error4"
assert fibonachchi_cycle(10) == fibonachchi_rec(10), "error5"
assert fibonachchi_cycle(-100) == fibonachchi_rec(-100), "error6"
assert fibonachchi_cycle(7) == fibonachchi_rec(7), "error7"
assert fibonachchi_cycle(30) == fibonachchi_rec(30), "error8"
assert fibonachchi_cycle(1) == fibonachchi_rec(1), "error9"
assert fibonachchi_cycle(-10000) == fibonachchi_rec(-10000), "error10"

fibonachchi_cycle(5)

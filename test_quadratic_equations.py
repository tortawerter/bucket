test = [
    [1, -2, -15],
    [1, 1, 1],
    [1, 1, 0],
    [-1, 0, 1],
    [1, 0, 1],
    [0, 1, 1],
    [1, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 0, 0]
]


def solve_quadratic_equations(a, b, c):
    if a == 0 and b == 0:
        return 'error, invalid data'
    elif a == 0 and b != 0 and c != 0:
        return ((-1 * c) / b, 0)
    elif a != 0 and b != 0 and c != 0:
        if b ** 2 + -1 * (4 * a * c) > 0:
            return (-b - (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a),\
                   (-b + (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a)
        else:
            return "dis < 0"
    elif a != 0 and b == 0 and c != 0:
        if ((-c) / a) < 0:
            return "error"
        else:
            return ((-c) / a) ** (1 / 2), -((-c) / a) ** (1 / 2)
    elif a != 0 and b != 0 and c == 0:
        return (((-b) / a), 0)
    elif (a != 0 and b == 0 and c == 0) or (a != 0 and b != 0 and c == 0) or (a == 0 and b != 0 and c == 0):
        return 0


assert solve_quadratic_equations(test[0][0], test[0][1], test[0][2]) == (-3, 5), f"error1"
assert solve_quadratic_equations(test[1][0], test[1][1], test[1][2]) == "dis < 0", f"error2"
assert solve_quadratic_equations(test[2][0], test[2][1], test[2][2]) == (-1, 0), f"error3"
assert solve_quadratic_equations(test[3][0], test[3][1], test[3][2]) == (1, -1), f"error4"
assert solve_quadratic_equations(test[4][0], test[4][1], test[4][2]) == "error", f"error5"
assert solve_quadratic_equations(test[5][0], test[5][1], test[5][2]) == (-1, 0), f"error6"
assert solve_quadratic_equations(test[6][0], test[6][1], test[6][2]) == 0, f"error7"
assert solve_quadratic_equations(test[7][0], test[7][1], test[7][2]) == "error, invalid data", f"error7"
assert solve_quadratic_equations(test[8][0], test[8][1], test[8][2]) == 0, f"error7"
assert solve_quadratic_equations(test[9][0], test[9][1], test[9][2]) == "error, invalid data", f"error8"
for elem in test:
    a = elem[0]
    b = elem[1]
    c = elem[2]
    print(f"{elem}, {solve_quadratic_equations(a, b, c)}")

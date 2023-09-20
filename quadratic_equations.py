def my_map(func, my_list):
    for h in range(len(my_list)):
        my_list[h] = func(my_list[h])
    return my_list


# a, b, c = my_map(float, input().split())
def solve_quadratic_equations(a, b, c):
    
    if a == 0 and b == 0:
        return 'error, invalid data'
    
    elif a == 0 and b != 0 and c != 0:
        return ((-1 * c) / b)
    
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


v = 10
a = 3
d = 5
s = 153
print(solve_quadratic_equations(d, (2 * v + 2 * a - d), -2 * s))

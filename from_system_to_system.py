def from_system_to_ten(num_input_first, system_input):
    num_output_first = 0
    str_num_system = str(num_input_first)
    for i in range(len(str_num_system)):
        num_output_first += int(str_num_system[i]) * system_input**(len(str_num_system) - (i+1))
    return num_output_first


def num_system(num_input, notation_num):
    str_num = ""
    while num_input != 0:
        str_num += str(num_input % notation_num)
        num_input = num_input // notation_num
    return str_num[::-1]


def all_together(n, k, m):
    return num_system(from_system_to_ten(n, k), m)


print(all_together(15, 10, 2))


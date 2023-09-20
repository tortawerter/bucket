def num_system(num_input, notation_num):
    str_num = ""
    while num_input != 0:
        str_num += str(num_input % notation_num)
        num_input = num_input // notation_num
    return str_num[::-1]


print(num_system(99, 4))

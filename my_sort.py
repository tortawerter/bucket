def sort(my_list):
    for h in range(len(my_list) - 1):
        for i in range(len(my_list) - h - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list


my_list = [1, 14, 5, 7, 10, 11, 12, 3, 16]
print(sort(my_list))
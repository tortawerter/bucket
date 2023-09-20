def my_map(func, my_list):
    for h in range(len(my_list)):
        my_list[h] = func(my_list[h])
    return my_list


print(my_map(float, input().split()))

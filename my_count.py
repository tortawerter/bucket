def my_count(my_list, elem):
    quantity = 0
    for i in range(len(my_list)):
        if my_list[i] == elem:
            quantity += 1
    return quantity


my_list = "hello, beautiful alien willy"
print(my_count(my_list, "l"))




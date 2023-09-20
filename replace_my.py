def my_count(my_list, elem):
    quantity = 0

    for i in range(len(my_list)):
        if my_list[i] == elem:
            quantity += 1
    return quantity


def my_replace(old_value, new_value, count=len("hello world")):
    count_old = 0
    my_list, final_replace = "hello, beautiful alien willy", ""
    for i in range(0, len(my_list)):
        if my_list[i] != old_value or i == count_old + count:
            final_replace = final_replace + my_list[i]
            count_old += 1
        else:
            final_replace = final_replace + new_value
    return final_replace


my_list = "hello, beautiful alien willy"
print(my_count(my_list, "l"))
print(my_replace("l", "k", 0))
test = [
    ["l", "m", 1],
    ["l", "m"],
    ["e", ".", 2],
    ["z", "0"],
    ["l", "82", 100],
    [",", "***", 2],
    [" ", "1", 2]
]
assert my_replace(test[0][0], test[0][1], test[0][2]) == "hemlo, beautiful alien willy", "error1"
assert my_replace(test[1][0], test[1][1]) == "hemmo, beautifum amien wimmy", "error2"
assert my_replace(test[2][0], test[2][1], test[2][2]) == "h.llo, b.autiful alien willy", "error3"
assert my_replace(test[3][0], test[3][1]) == "hello, beautiful alien willy", "error4"
assert my_replace(test[4][0], test[4][1], test[4][2]) == "he8282o, beautifu82 a82ien wi8282y", "error5"
assert my_replace(test[5][0], test[5][1], test[5][2]) == "hello*** beautiful alien willy", "error6"
assert my_replace(test[6][0], test[6][1], test[6][2]) == "hello,1beautiful1alien willy", "error6"

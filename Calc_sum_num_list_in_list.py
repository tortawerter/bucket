def CalcSumNumbers(list_in_list):  # [ -2, 3, 8, 11, [-4, 6, [ 2, [-5, 4] ] ] ]
    ans = 0
    for elem in list_in_list:
        if not isinstance(elem, list):
            ans += elem
        else:
            ans += CalcSumNumbers(elem)
    return ans


L = [[-2, 3, 8, 11, [-4, 6, [2, [-5, 4]]]],
     [1, [2, [3, [4]]]],
     [[0, [0, [0, [0, []], [0]]]]],
     [0, [0], 0, 0, [0, [0, [-4]], 0, [0, 0, [0, 0]]]],
     [],
     [0, 0, 0],
     [[[[[[[[[0]]]]]]]]]]

assert CalcSumNumbers(L[0]) == 23, "error1"
assert CalcSumNumbers(L[1]) == 10, "error2"
assert CalcSumNumbers(L[2]) == 0, "error3"
assert CalcSumNumbers(L[3]) == -4, "error4"
assert CalcSumNumbers(L[4]) == 0, "error5"
assert CalcSumNumbers(L[5]) == 0, "error6"
assert CalcSumNumbers(L[6]) == 0, "error7"

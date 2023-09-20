def CalcSumNumbers(current_list):  # [2, 3, 8, 11, 4, 6]
    if not current_list:
        return 0
    else:
        ans = CalcSumNumbers(current_list[1:])
        ans += current_list[0]
        return ans


print(CalcSumNumbers([2, 3, 8, 11, 4, 7]))

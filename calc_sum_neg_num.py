def CalSumNegNum(list_str):  # [-2, 3, 8, -11, -4, 6]
    if not list_str:
        return 0
    else:
        ans = CalSumNegNum(list_str[1:])
        if list_str[0] < 0:
            ans += 1
        return ans


print(f"n = {CalSumNegNum([-2, 3, 8, -11, -4, 6])}")

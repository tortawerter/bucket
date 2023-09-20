def remove_palindrom(s):
    if s == s[::-1]:
        return 1
    else:
        return 2

print(remove_palindrom("baaababaaab"))

strs = ["flower", "flow", "flight"]
def f(strs):

    shortest = min(strs, key=len)

    for i, char in enumerate(shortest):
        for string in strs:
            if string[i] != char:
                print(shortest, shortest[:i])
                return shortest[:i]
    return shortest

print(f(strs))

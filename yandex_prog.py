def brackets(current, open_count, close_count, n):
    if open_count == n and close_count == n:
        print(current)
    if open_count < n:
        brackets(current + "(", open_count + 1, close_count, n)
    if close_count < open_count:
        brackets(current + ")", open_count, close_count + 1, n)


brackets("", 0, 0, 4)

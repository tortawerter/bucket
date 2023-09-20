matrix = [
    [2, 1, 1, 1, 1, 2, 3],
    [2, 2, 2, 2, 2, 2, 6],
    [3, 3, 3, 3, 3, 3, 8],
    [4, 4, 4, 4, 4, 4, 19],
    [5, 5, 5, 5, 5, 5, 9],
    [6, 6, 6, 6, 6, 100, 101]
]
sum = 0
for i in range(0, len(matrix)):
    for n in range(0, len(matrix)):
        if i == n:
            sum = matrix[i][n] + sum
            matrix[i][n] = sum
            print(sum)
print('sum:', sum)
for arr in matrix:
    print(arr)

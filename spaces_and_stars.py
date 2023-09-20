matrix = [1,  '                          ', 2, 'Timofey', 3, '   ', 4,  5,  5, ' ', 6]
for i in range(0, len(matrix)):
    if type(matrix[i]) == str:
        matrix[i] = matrix[i].replace(' ', '*')
print(matrix)

a = "   "
print()
rep = a[0].replace(' ', '*')
print(rep)

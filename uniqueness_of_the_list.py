import random
list = range(100)
list = random.choices(list, k=10)
print(sorted(list))
solution = True
for elem in range(len(list) - 1):
    for new_elem in range(elem + 1, len(list)):
        if list[elem] == list[new_elem]:
            solution = False
print(solution)

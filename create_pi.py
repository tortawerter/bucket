import numpy as np
import random
print(np.pi)
count_range = 0
uniq = [0]
for i in range(10000000000):
    count_range += 1
    num_1 = random.randint(1, 9999999999)
    num_2 = random.randint(1, 9999999999)

    print("NUM_1: ", num_1, "NUM_2", num_2, "divide: ", num_1 / num_2, "or", num_2 / num_1)
    if count_range == 10000000000:
        print("цикл закончен")
    if num_1 / num_2 == np.pi or num_2 / num_1 == np.pi:
        break
print(num_1, num_2)
print(num_1 / num_2)

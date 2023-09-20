amount = int(input("введите количество: "))
counter, max_counter = 0, 0
bin_str = ""

for bin_num in range(amount):
    bin = input("введите число: ")
    bin_str += bin

    if bin_str[bin_num] == "1":
        counter += 1

        if counter > max_counter:
            max_counter = counter

    else:
        counter = 0

print(max_counter)

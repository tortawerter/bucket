import matplotlib.pyplot as plt

x = []
y = []

for bracket in range(1, 12):
    counter = 0
    def yandex(opened_brackets, closed_brackets, result, bracket):
        global counter
        if opened_brackets + closed_brackets == bracket * 2:
            counter += 1
        if bracket > opened_brackets:
            yandex(opened_brackets + 1, closed_brackets, result + "(", bracket)
        if opened_brackets > closed_brackets:
            yandex(opened_brackets, closed_brackets + 1, result + ")", bracket)


    yandex(0, 0, "", bracket)
    print(counter)

    x.append(counter)
    y.append(bracket)

plt.plot(x, y)
plt.grid()
plt.show()

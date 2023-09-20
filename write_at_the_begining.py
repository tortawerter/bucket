information = "123"


def begining(file_name, information):
    with open(file_name, "r") as test:
        test_text = test.read()
    with open("test_2.txt", "w") as test:
        test.write(information)
        test.write('\n')
        test.write(test_text)
    with open("test_2.txt") as test:
        return test.read()


print(begining("test.txt", information))

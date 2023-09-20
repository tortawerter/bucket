def file_system(frist_file, second_file):
    with open(frist_file, "r") as take:
        take_text = take.read()
    with open(second_file, "w") as give:
        give.write(take_text)
    with open(second_file, "r") as give:
        return give.read()


print(file_system("test.txt", "test_2.txt"))

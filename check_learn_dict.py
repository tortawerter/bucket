def learn_dict(text_test):
    punct = [".", ",", "?", "!", "…", ";", "-", ":", "\"", "\"", "\'", "\'", "(", ")", "[", "]"]

    for rep in text_test:
        if rep in punct:
            text_test = text_test.replace(rep, "")

    text_test = text_test.split()
    dict_for_test = {}

    for word in text_test:
        if word in dict_for_test:
            dict_for_test[word] += 1
        else:
            dict_for_test[word] = 1
    for n in dict_for_test.items():
        if n[1] == max(dict_for_test.values()):
            return n[0], dict_for_test


text_test = "goodbye, alien, goodbye."
print(learn_dict(text_test))

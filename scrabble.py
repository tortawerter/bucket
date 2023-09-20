eng = "AEIOULNSTRDGBCMPFHVWYKJXQZ"
eng += eng.lower()
rus = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
rus += rus.lower()
word = input("введите слово: ")

dict_eng = {
    1: "AEIOULNSTR",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

dict_rus = {
    1: "ЕОТАИСНВР",
    2: "ПЛУМДК",
    3: "ЯГЬБ",
    4: "ЙЫ",
    5: "ЗЖЧХЦ",
    8: "ШЮЭ",
    10: "ЪЩФ"
}


def isCyrillic(eng, rus, word):
    result = None

    if word[0] in eng:
        result = False

    elif word[0] in rus:
        result = True

    return result


def scrabble(dict_eng, dict_rus, result, word):
    points = 0

    if result == False:
        for i in word.upper():
            for key, value in dict_eng.items():
                if i in value:
                    points += key

    elif result == True:
        for i in word.upper():
            for key, value in dict_rus.items():
                if i in value:
                    points += key

    return points


print(scrabble(dict_eng, dict_rus, isCyrillic(eng, rus, word), word))


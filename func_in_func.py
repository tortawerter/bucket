def text_one(start_text, end_text, *text):
    text_final = ""
    for i in range(len(text)):
        text_final += text[i] + " "
    final = start_text + " " + text_final + " " + end_text
    final = final.replace("  ", " ")
    return final


text = "пошел в магазин", "ушел из дома", "вернулся домой"
start_text, end_text = "hello", "world"
print(text_one(start_text, end_text, "пошел в магазин", "ушел из дома", "вернулся домой"))

# убрать пробел между домой и world

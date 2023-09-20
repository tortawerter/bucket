def dict_keys(dict_one, values_dict, new_value):
    result = []
    counter = 0
    for key, value in dict_one.items():
        if values_dict == value:
            counter += 1
            result += key
            dict_one[key] = new_value
    return dict_one, counter


dict_one = {
    "a": "1", "b": "2",
    "c": "1", "f": "2"
}
values_dict = "2"
new_value = "Billy"
print(dict_keys(dict_one, values_dict, new_value))

dict_1 = {2: "two", 4: "four", 6: "six"}
key = 4
def get_value(dict_1, key):
    if key in dict_1:
        print(dict_1.get(key))
        return dict_1.get(key)
    else:
        print(key, "is not key of dict_1")
        return None
get_value(dict_1, key)
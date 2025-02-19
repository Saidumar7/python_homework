dict_1 = {2: "two", 4: "four", 6: "six"}
def count_keys(dict_1):
    return len(dict_1)
if count_keys(dict_1) == 0:
    print("dict_1 is empty")
else:
    print("Number of keys in dict_1 is", count_keys(dict_1))
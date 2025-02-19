dict_1 = {2: "two", 4: "four", 6: "six"}
lst = []
for key in dict_1:
    lst.append(dict_1.get(key))
print("List containing all values of given dictionary is",lst)
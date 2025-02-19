set_1 = {2, 4, 6}
element = 4
if element in set_1:
    set_1.remove(element)
    print(element, "is removed from set_1", set_1)
else:
    print(element, "is not element of set_1", set_1)
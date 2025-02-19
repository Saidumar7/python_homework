set_1 = {2, 4, 6}
element = 5
def add_element(set_1, element):
    if element not in set_1:
        set_1.add(element)
        print(element, "is added to set_1", set_1)
    else:
        print(element, "is already element of set_1", set_1)
add_element(set_1, element)
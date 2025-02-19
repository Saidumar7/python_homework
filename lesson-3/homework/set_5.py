set_1 = {2, 4, 6}
element = 4
def is_element(set_1, element):
    return element in set_1
if is_element(set_1, element):
    print(element, "is element of set_1")
else:
    print(element, "is not element of set_1")
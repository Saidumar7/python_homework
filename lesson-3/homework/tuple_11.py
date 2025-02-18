given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 1, 4, 2, 1)
def indices_of_element(given_tuple, element):
    return [index for index, value in enumerate(given_tuple) if value == element]
element = 1
print("Indices of the" ,element, "are", indices_of_element(given_tuple, element))
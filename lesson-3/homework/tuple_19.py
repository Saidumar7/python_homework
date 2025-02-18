given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 1, 4, 2, 1)
element = 3
lst = list(given_tuple)
lst.remove(element)
new_tuple = tuple(lst)
print("Tuple after removing the element", element, "is", new_tuple)
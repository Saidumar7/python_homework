given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 1, 4, 2, 1)
new_tuple = tuple(set(given_tuple))
print("Tuple after removing duplicates is", new_tuple)
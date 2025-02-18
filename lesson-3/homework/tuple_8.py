given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 1, 4, 2, 1)
def slice_tuple(given_tuple):
    new_tuple = given_tuple[:3]
    return new_tuple
print("First three elements of the tuple are", slice_tuple(given_tuple))
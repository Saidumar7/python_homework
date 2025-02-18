given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 1, 4, 2, 1)
def first_element(given_tuple):
    if len(given_tuple) == 0:
        return None
    else:
        return given_tuple[0]
print("First element in the tuple is", first_element(given_tuple))
given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 1, 4, 2, 1)
def second_min_element(given_tuple):
    return sorted(set(given_tuple))[1]
print("Second minimum element in the tuple is", second_min_element(given_tuple))
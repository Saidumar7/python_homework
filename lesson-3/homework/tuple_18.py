given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 1, 4, 2, 1)
subtuple = (1, 3, 9)
def min_of_subtuple(subtuple):
    min_subtuple = min(subtuple)
    return min_subtuple
print("Minimum element in the subtuple", subtuple, "is", min_of_subtuple(subtuple))
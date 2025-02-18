given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 1, 4, 2, 1)
subtuple = (1, 3, 1)
def max_of_subtuple(subtuple):
    max_subtuple = max(subtuple)
    return max_subtuple
print("Maximum element in the subtuple",subtuple, "is", max_of_subtuple(subtuple))
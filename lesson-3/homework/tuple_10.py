given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 1, 4, 2, 1)
def is_empty(given_tuple):
    if len(given_tuple) == 0:
        print("The tuple is empty")
        return True
    else:
        print("The tuple is not empty")
        return False
is_empty(given_tuple)
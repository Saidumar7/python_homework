given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 1, 4, 2, 1)
def is_sorted(given_tuple):
    if given_tuple == tuple(sorted(given_tuple)):
        return True
    else:    
        return False
if is_sorted(given_tuple):
    print("The tuple is sorted")
else:
    print("The tuple is not sorted")